import torch
from models import Practice

if __name__ == "__main__":
    model = Practice()
    tensor = torch.ones(32, 3, 128, 128)
    model.forward(tensor)