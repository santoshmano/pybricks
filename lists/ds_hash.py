class DirectHashMap:
    """
    Hash map which just replaces when there is a collision
    """
    def __init__(self, num_buckets):
        self.num_buckets = num_buckets
        self.bucket = [None for _ in range(num_buckets)]

    def _set(self, key, val):
        #set or replace blindly
        self.bucket[self._hash(key)] = val
        return

    def _get(self, key):
        val = self.bucket[self._hash(key)]

        if val.key == key:
            return val

        return None

    def _hash(self, key):
        return key % self.num_buckets

    def __getitem__(self, key):
        return self._get(key)

    def __setitem__(self, key, value):
        self._set(key, value)

    def __str__(self):
        return str([self.bucket[i] for i in range(self.num_buckets)])

if __name__ == "__main__":
    h = DirectHashMap(10)
    print(h)

    for i in range(1999):
        h[i] = "hello"
    print(h)
    for i in range(1999, 2002):
        h[i] = "bye"
    print(h)
    h[10] = "hello"
    print(h)
