import torch
from torch import nn

class MyModule(nn.Module):
    def __init__(self):
        super().__init__()
        self.mytensor = torch.full((3,3), 3.0)
        self.elem_add = 4
        self.elem_multiply = 6
    
    def forward(self,x):
        x1 = x + self.mytensor
        x2 = x1 + self.elem_add
        x3 = x2 * self.elem_multiply
        print("==== problem 2 ====")
        print(x1)
        print("==== problem 3 ====")
        print(x2)
        print("==== problem 4 ====")
        print(x3)

if __name__ == "__main__":
    x = torch.zeros((3,3))
    module = MyModule()
    module.forward(x)