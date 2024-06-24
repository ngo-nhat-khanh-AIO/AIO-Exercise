import torch
import torch.nn as nn

class Softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        sum_exp_x = torch.sum(exp_x, dim=-1, keepdim=True)
        return exp_x / sum_exp_x

class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_max = torch.max(x, dim=0, keepdims=True)
        x_exp = torch.exp(x - x_max.values)
        partition = x_exp.sum(0, keepdims=True)
        return x_exp / partition

if __name__ == "__main__":
    num_1 = torch.tensor([1.0, 2.0, 3.0])
    num_2 = torch.tensor([1.0, 2.0, 3.0])
    softmaxstable = SoftmaxStable()
    softmax = Softmax()
    print(softmax(num_1))
    print(softmaxstable(num_2))