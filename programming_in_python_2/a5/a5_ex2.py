import torch
from torch.utils.data import DataLoader
from tqdm import tqdm 
import matplotlib.pyplot as plt 

def training_loop(network: torch.nn.Module,
                train_data: torch.utils.data.Dataset,
                eval_data: torch.utils.data.Dataset,
                num_epochs: int,
                batch_size: int,
                learning_rate: float,
                show_progress: bool = False
                ) -> tuple[list, list]:
    
    optimizer = torch.optim.Adam(network.parameters(), lr=learning_rate)
    
    training_loader = DataLoader(train_data,
                        shuffle=False,
                        batch_size=batch_size,
                        num_workers=0
                        )
    
    eval_loader = DataLoader(eval_data,
                    shuffle=False,
                    batch_size=batch_size,
                    num_workers=0
                    )
    
    train_losses, eval_losses = [], []
    loss_f = torch.nn.MSELoss()

    for i in range(num_epochs):
        network.train()
        minibatch_loss_train = 0
        nr_batches_train = 0

        loop_train = tqdm(training_loader, desc=f"train epoch {i}") if show_progress else training_loader
        for input, target in loop_train:
            output = network(input)
            output = output.flatten()
            loss = loss_f(output, target)

            loss.backward()
            optimizer.step()
            optimizer.zero_grad()

            minibatch_loss_train += loss.item()
            nr_batches_train+=1

        average_loss_train_i = minibatch_loss_train / nr_batches_train
        train_losses.append(average_loss_train_i)

        ########

        network.eval()
        minibatch_loss_eval = 0
        nr_batches_eval = 0

        with torch.no_grad():
            for input, target in eval_loader:
                output = network(input)
                output = output.flatten()

                loss = loss_f(output, target)

                minibatch_loss_eval += loss.item()
                nr_batches_eval+=1

        average_loss_eval_i = minibatch_loss_eval / nr_batches_eval
        eval_losses.append(average_loss_eval_i)

        if i == 0:
            min_loss = average_loss_eval_i
            no_improvement = 0

        if min_loss > average_loss_eval_i: # ugly, but checks if previous loss is bigger than current loss, if yes, resets
            no_improvement = 1
            min_loss = average_loss_eval_i
        else:
            no_improvement+=1

        if no_improvement == 7:
            break

    return (train_losses, eval_losses)

def plot_losses(train_losses, eval_losses):
    x = [i for i in range(len(train_losses))]

    plt.plot(x, train_losses, label = "train losses", color='plum') 
    plt.plot(x, eval_losses, label = "eval losses", color='deeppink') 
    
    plt.xlabel("epoch")
    plt.ylabel("MSE value")

    plt.xticks(x)
    plt.legend() 
    
    plt.savefig('epoch_loss.pdf')

if __name__ == "__main__":
    from a4_ex1 import SimpleNetwork
    from dataset import get_dataset
    torch.random.manual_seed(1234)
    train_data, eval_data = get_dataset()
    network = SimpleNetwork(32, [128, 64, 128], 1, True)
    train_losses, eval_losses = training_loop(network, train_data, eval_data, num_epochs=100, batch_size=16, learning_rate=1e-3)
    plot_losses(train_losses, eval_losses)