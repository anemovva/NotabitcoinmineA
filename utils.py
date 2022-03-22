import array
from collections import OrderedDict

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


def makeaction(movement, attack, craft, smelt):
    action = OrderedDict([('attack', array()), ('back', array(0)), ('camera', array([  0, 0], dtype=float32)), ('craft', 'None'), ('equip', 'None'), ('forward', array(0)), ('jump', array(0)), ('left', array(0)), ('nearbyCraft', 'None'), ('nearbySmelt', 'None'), ('place', 'None'), ('right', array(0)), ('sneak', array(0)), ('sprint', array(0))])

    movement = movement.squeeze().tolist()
    action['attack'] = movement[0]
    action['back'] = movement[1]
    action['forward'] = movement[2]
    action['left'] = movement[3]
    action['right'] = movement[4]
    action['jump'] = movement[5]
