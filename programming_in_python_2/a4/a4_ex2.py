import torch
import torch.nn as nn

class SimpleCNN(nn.Module):
    def __init__(self,
                input_channels: int,
                hidden_channels: list,
                use_batchnormalization: bool,
                num_classes: int,
                kernel_size: list,
                activation_function: torch.nn.Module = torch.nn.ReLU()):
        super().__init__()
        layers = []
        in_features=input_channels
        for i, channel in enumerate(hidden_channels):
            layer = nn.Conv2d(in_channels=in_features, 
                              out_channels=channel, 
                              kernel_size=kernel_size[i], 
                              padding=kernel_size[i]//2)
            layers.append(layer)
            layers.append(activation_function)

            if use_batchnormalization:
                layers.append(nn.BatchNorm2d(channel))

            in_features = channel

        self.layers = nn.Sequential(*layers)
        self.flatten = nn.Flatten() 
        self.output_layer = nn.Linear(in_features=in_features*70*100, out_features=num_classes)
    
    def forward(self, input_images: torch.Tensor):
        x = self.layers(input_images)
        x = self.flatten(x)
        return self.output_layer(x)

if __name__ == "__main__":
    torch.random.manual_seed(1234)
    network = SimpleCNN(3, [32, 64, 128], True, 10, [3, 5, 7], activation_function=nn.ELU())
    input = torch.randn(1, 3, 70, 100, requires_grad = False)
    output = network(input)
    print(output)