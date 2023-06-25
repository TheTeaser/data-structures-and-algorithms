class HashTable():
    def __init__(self, size=1024):
        self.max = size
        self.arr = [[] for _ in range(self.max)]

    def get_hash(self, key):
        h = 5381
        for char in key:
            h = (h * 33 + ord(char)) % self.max
        return h



    def add(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
        if not found:
            self.arr[h].append((key, value))

    def get(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def contains(self, key):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                found = True
        return found

    def delete(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]
