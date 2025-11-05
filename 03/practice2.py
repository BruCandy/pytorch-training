import torch
from torch import nn

if __name__ == "__main__":
    tensor = torch.ones(32, 1024)
    li = nn.Linear(in_features=1024, out_features=256, bias=True)
    out1 = li(tensor)
    print(f"{out1.shape}")
    li2 = nn.Linear(in_features=1024, out_features=2048, bias=True)
    out2 = li2(tensor)
    print(f"{out2.shape}")
    out3 = out1.reshape(32, 16, 16)
    print(f"{out3.shape}")
     
