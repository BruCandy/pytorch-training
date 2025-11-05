from torch import nn

class Practice(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=256, kernel_size=5, stride=8),
            nn.BatchNorm2d(num_features=256),
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(in_features=65536, out_features=64)
        )
    
    def forward(self, x):
        out = self.net(x)
        print(f"{out.shape}")