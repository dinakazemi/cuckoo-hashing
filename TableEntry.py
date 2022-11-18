"""
An entry in the HashTable.

The key of the entry that is hashed.
"""

class TableEntry:

        def __init__(self, k, v):
                """
                Initialises the Table Entry by assigning a
                Key, Value and setting the "Visited" to false.
                :param k:
                :param v:
                """
                self.k = k
                self.v = v

        def get_key(self):
                """
                Get the entry's key.
                :return: The entry's key.
                """
                return self.k

        def get_value(self):
                """
                Get the entry's value.
                :return:  The entry's value.
                """
                return self.v
