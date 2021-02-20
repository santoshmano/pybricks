class Txn:
    def __init__(self):
        self.txndb = dict()
        self.txn_reversedb = dict()


class MemoryDB:
    def __init__(self):
        self.memdb = dict()
        self.reversedb = dict()
        self.txns = list()
        self.txn_level = 0

    def get(self, key):
        if self.txn_level:
            if key in self.txns[self.txn_level-1].txndb:
                return self.txns[self.txn_level-1].txndb[key]

        if key in self.memdb:
            return self.memdb[key]
        return None

    def set(self, key, value):
        if self.txn_level:
            self.txns[self.txn_level-1].txndb[key] = value
            print("dbg - in txn", self.txn_level)
            if value in self.txns[self.txn_level-1].txn_reversedb:
                self.txns[self.txn_level-1].txn_reversedb += 1
            else:
                self.txns[self.txn_level-1].txn_reversedb = 1
            return

        self.delete(key)
        self.memdb[key] = value
        if value in self.reverse_db:
            self.reverse_db[value] += 1
        else:
            self.reverse_db[value] = 1

    def delete(self, key):
        if key in self.memdb:
            value = self.memdb[key]
            if self.reverse_db[value] == 1:
                del self.reverse_db[value]
            else:
                self.reverse_db[value] -= 1
            del self.memdb[key]

    def count(self, value):
        if value in self.reverse_db:
            return self.reverse_db[value]
        return 0

    def begin(self):
        self.txn_level += 1
        self.txns.append(Txn())

    def rollback(self):
        if self.txn_level:
            self.txns.pop()
            self.txn_level -= 1

    def commit(self):
        while self.txn_level:
            txn = self.txns.pop()
            #process txn
            self.txn_level -= 1

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.set(key, value)
        return

def test1():
    print("Test1")
    memDB = MemoryDB()

    memDB.set("a", 10)
    print(memDB.get("a"))
    memDB.delete("a")
    print(memDB.get("a"))

    return

def test2():
    print("Test2")
    memDB = MemoryDB()

    memDB.set("a", 10)
    memDB.set("b", 10)
    print(memDB.count(10))
    print(memDB.count(20))
    memDB.delete("a")
    print(memDB.count(10))
    print(memDB.set("b", 30))
    print(memDB.count(10))

    return

def test3():
    print("Test3")
    memDB = MemoryDB()

    memDB.begin()
    memDB.set("a", 10)
    print(memDB.get("a"))

    memDB.begin()
    memDB.set("a", 20)
    print(memDB.get("a"))
    memDB.rollback()

    print(memDB.get("a"))
    memDB.rollback()

    print(memDB.get("a"))

if __name__ == "__main__":

    test1()
    #test2()
    #test3()
