from ds_doubly_linked_q import DoublyLinkedQ

class Node:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:
    """
    A least recently used cache with a max capacity to hold items.
    It uses
        - a queue with a doubly linked node with a pointer(key) to a _hash map
        - and a _hash map to index into the q, for O(1) access time.
    """
    def __init__(self, max_cap=256):
        self.max_cap = max_cap
        self._hash = {}
        self.q = DoublyLinkedQ()

    def set(self, key, val):
        """
        Update the cache with a new value. The value is stored in a node.
        Add the node to the beginning of the lru q.

        :param key: key used to reference the value
        :param val: value being cached, can be anything really.
        :return: Nothing.
        """
        if key in self._hash:
            n = self._hash[key]
            self.q.unlink(n)
        else:
            if self.q.len <= self.max_cap:
                # create a new node
                n = Node(val, key)
            else:
                # remove an old node and reuse it
                n = self.q.get_oldest()
                self.q.unlink(n)
                self._hash[n.key] = None

        n.val = val
        self.q.enqueue_head(n)
        self._hash[key] = n

        return

    def get(self, key):

        n = self._hash[key]
        if n is not None:
            self.q.unlink(n)
            self.q.enqueue_head(n)
            val = n.val
        else:
            val = None

        return val

    def remove(self, key):
        """
        remove an entry from the lru cache and de-allocate all its resources
        :param key:
        :return:
        """
        if key in self._hash:
            n = self._hash[key]
            self.q.unlink(n)
            self._hash[key] = None
            del n

        return

    def evict(self, num):
        """
        evict n least recently used entries from the cache
        """

        for _ in range(num):
           self.remove(self.q.get_oldest().key)



if __name__ == "__main__":
    cache = LRUCache()

    for i in range(1,11):
        print(i)
        cache.set(i, 12120+i)

    for i in range(1,11):
        print(cache.get(i))

    for i in range(5,11):
        cache.remove(i)

    print("After remove")
    for i in range(1,11):
        print(cache.get(i))

    print("getting 4", cache.get(4))

    print("After evicting 2")
    print(cache.evict(2))

    for i in range(1,11):
        print(cache.get(i))
