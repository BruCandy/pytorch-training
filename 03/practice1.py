import torch
from torch import nn

if __name__ == "__main__":
    tensor = torch.ones(32, 3, 128, 128)
    conv1 = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3)
    out1 = conv1(tensor)
    print(f"{out1.shape}")
    conv2 = nn.Conv2d(in_channels=3, out_channels=256, kernel_size=3, stride=2, padding=1)
    out2 = conv2(tensor)
    print(f"{out2.shape}")
    conv3 = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=5, padding=1)
    out3 = conv3(tensor)
    print(f"{out3.shape}")
    conv4 = nn.Conv2d(in_channels=3, out_channels=256, kernel_size=5, stride=2, padding=2)
    out4 = conv4(tensor)
    print(f"{out4.shape}")

     
