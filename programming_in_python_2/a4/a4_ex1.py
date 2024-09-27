import torch
import torch.nn as nn

class SimpleNetwork(nn.Module):
    def __init__(self,
                input_neurons: int,
                hidden_neurons: list,
                output_neurons: int,
                use_bias: bool,
                activation_function: torch.nn.Module = torch.nn.ReLU()):
        super().__init__()
        self.activation_function = activation_function

        self.layer_0 = nn.Linear(in_features=input_neurons, out_features=hidden_neurons[0], bias=use_bias)
        self.layer_1 = nn.Linear(in_features=hidden_neurons[0], out_features=hidden_neurons[1], bias=use_bias)
        self.layer_2 = nn.Linear(in_features=hidden_neurons[1], out_features=hidden_neurons[2], bias=use_bias)
        self.layer_3 = nn.Linear(in_features=hidden_neurons[2], out_features=output_neurons, bias=use_bias)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.layer_0(x)
        x = self.activation_function(x)
        x = self.layer_1(x)
        x = self.activation_function(x)
        x = self.layer_2(x)
        x = self.activation_function(x)
        x = self.layer_3(x)
        return x

if __name__ == "__main__":
    torch.random.manual_seed(1234)
    simple_network = SimpleNetwork(40, [10, 20, 30], 5, True)
    input = torch.randn(1, 40, requires_grad = False)
    output = simple_network(input)
    print(output)