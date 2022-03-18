import torch.nn as nn
import torch


class MineNet(nn.Module):
    def __init__(self, env) -> None:
        super().__init__()

        self.framecnn = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size = 3),
            nn.ReLU(),

            nn.Conv2d(32, 64, kernel_size = 3),
            nn.ReLU(),

            nn.Conv2d(64, 128, kernel_size = 3),
            nn.ReLU(),

            nn.Conv2d(128, 256, kernel_size = 3),
            nn.ReLU(),

            nn.Flatten(),

            nn.Linear(256*64*64, 512)
            
        )

        self.pastmemory = nn.LSTM()

        

