class Hashtable:
    def __init__(self):
        """
        Initializes a new instance of the Hashtable class.
        """
        self.table = {}

    def add(self, key, value):
        """
        Adds a key-value pair to the hashtable.
        """
        self.table[key] = value

    def contains(self, key):
        """
        Checks if a key exists in the hashtable.
        """
        return key in self.table


def left_join(synonyms, antonyms):
    """
    A function that combines two HashTables, where the first table returns fully but with the same records only from the second HashTable.
    """
    result = []
    for key in synonyms.table:
        if synonyms.contains(key) and antonyms.contains(key):
            result.append([key, synonyms.table[key], antonyms.table[key]])
        else:
            result.append([key, synonyms.table[key], None])
    return result

#Synonyms HashTable:
synonyms = Hashtable()
synonyms.add("diligent", "employed")
synonyms.add("fond", "enamored")
synonyms.add("guide", "usher")
synonyms.add("outfit", "garb")
synonyms.add("wrath", "anger")

#Antonyms HashTable:
antonyms = Hashtable()
antonyms.add("diligent", "idle")
antonyms.add("fond", "averse")
antonyms.add("guide", "follow")
antonyms.add("flow", "jam")
antonyms.add("wrath", "delight")

result = left_join(synonyms, antonyms)
print(result)
