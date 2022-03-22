from calendar import c
from numpy import *
import array
from collections import OrderedDict
import torch.nn as nn
import torch


class MineNet(nn.Module):
    def __init__(self) -> None:
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

        self.actiondecider = nn.Linear(512+18, 3)

        self.movement = nn.Linear(512+18, 6)

        self.pastmemory = nn.LSTM(512+18, 512)

        self.softmax = nn.Softmax()

    def forward(self, frame, inventory, mem=None):

        x = self.framecnn(frame)

        x.append(inventory)
        x, mem = self.pastmemory(x, mem)

        actions = self.actiondecider(x)

        likelyaction = actions.argmax()

        movement = torch.zeros((6))
        craft = torch.zeros()
        smelt = torch.zeros()

        if (likelyaction ==0):
            movement = self.movement(x)
        elif (likelyaction==1):
            craft = torch.zeros()
            smelt = torch.zeros()
        else:            
            attack = 1
        return (self.softmax(movement), self.softmax(attack), craft, smelt), mem
    
   