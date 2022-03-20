
from numpy import nested_iters


class ItemManager():
    def __init__(self) -> None:
        self.item2index = {}
        self.index2item = {}
        self.nitems = 0

    def additem(self, item):
        self.item2index[item] = self.nitems
        self.index2item[self.nitems] = item
        self.nitems += 1

    def numitems(self):
        return self.nitems
    
