
class SkipNode:
    def __init__(self, val, height=1):
        self.val = val
        self.next = [None] * height


class SkipList:
    def __init__(self, maxheight):
        self.maxheight = maxheight
        self.len = 0
        self.head = SkipNode(None, maxheight)

    def random_level(self):
        level = 1
        while random.random() & 0x1:
            level += 1
        return  level

    def lookup(self):

    
