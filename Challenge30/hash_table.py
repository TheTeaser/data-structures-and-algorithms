class HashTable():
    def __init__(self, size=1024):
        '''
        Initilizes the Hashtable object.
        '''
        self.max = size
        self.arr = [[] for _ in range(self.max)]

    def get_hash(self, key):
        '''
        This method calculates the hash value for the keys.
        '''
        h = 5381
        for char in key:
            h = (h * 33 + ord(char)) % self.max
        return h

    def add(self, key, value):
        '''
        Adds data with the key to the hash table.
        '''
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
        if not found:
            self.arr[h].append((key, value))

    def get(self, key):
        '''
        Retrieves the data assocaited with the given key.
        '''
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def contains(self, key):
        '''
        Checks the hashtable if it contatins a given key.
        '''
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                found = True
        return found

    def delete(self, key):
        '''
        Deletes data and it's key from the hashtable.
        '''
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]
