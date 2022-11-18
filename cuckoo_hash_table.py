"""
Cuckoo Hash Table Implementation

Implements a hash table which utilises `CuckooHashing` to place elements into
the table.
"""

import TableEntry
import HashTableInterface
from linear_hash import LinearHashFunction
from functools import reduce
import linear_hash

class CuckooHashTable(HashTableInterface.HashTableInterface):
        def __init__(self, m, prng_one, prng_two):
                """
                Initialises the table with the correct hashes.
                :param m: The size of the table.
                :param h1n: The first variant of the hash.
                :param h2n:  The second variant of the hash.
                :param prng_one: Seeded Pseudo Random Number Generator for h1.
                :param prng_two: Seeded Pseudo Random Number Generator for h2.
                """

                self.size = m
                self.h1 = LinearHashFunction(m, prng_one)
                self.h2 = LinearHashFunction(m, prng_two)
                self.table = [None for i in range(0, m)]
                self.M = m
                self.added_elements = []
	
        def __repr__(self):
                """
                toString method; please do not modify!
                """
                s = "[{}]".format(
                        reduce(
                                (lambda a, b: "{}{}".format(a, b)),
                                map(lambda x: "-" if x is None else x.get_value(), self.table)
                            )
                )
                return s
		
        def put(self, k, v):
                """
                Puts the value into an entry into the table.
                :param k: The key for the matching value.
                :param v: The value to place into the table.
                        :return: true if the value was placed, else false. 
                """
                # TODO implement cuckoo hashing to put the value into the table.
                
                #create the table entry
                new_entry = TableEntry.TableEntry(k,v)
                
                #try to put the item into h1
                if (self.table[self.h1.__call__(k)] == None):
                        #print ("condition 1")
                        self.table[self.h1.__call__(k)] = new_entry
                        self.added_elements.append(new_entry)
                        return True
                if (self.table[self.h1.__call__(k)] != None and self.table[self.h1.__call__(k)].get_key() == k):
                        #print ("condition 2")
                        self.table[self.h1.__call__(k)] = new_entry
                        self.added_elements.append(new_entry)
                        return True
                #try to put into h2
                if (self.table[self.h2.__call__(k)] == None):
                        #print ("condition 3")
                        self.table[self.h2.__call__(k)] = new_entry
                        self.added_elements.append(new_entry)
                        return True
                if (self.table[self.h2.__call__(k)] != None and self.table[self.h2.__call__(k)].get_key() == k):
                        #print ("condition 4")
                        self.table[self.h2.__call__(k)] = new_entry
                        self.added_elements.append(new_entry)
                        return True
                #start eviction cycle
                counter = 0
                i=1
                while (True):
                        if (i == 1):
                                
                                #print ("value " + str_value + " being inserted.")
                                if (self.table[self.h1.__call__(new_entry.get_key())] == None):
                                        #print ("eviction finished at i=1")
                                        self.table[self.h1.__call__(new_entry.get_key())] = new_entry
                                        self.added_elements.append(new_entry)
                                        return True
                                if (self.table[self.h1.__call__(new_entry.get_key())] != None and self.table[self.h1.__call__(new_entry.get_key())].get_key() == new_entry.get_key()):
                                        #print ("condition 2")
                                        self.table[self.h1.__call__(new_entry.get_key())] = new_entry
                                        self.added_elements.append(new_entry)
                                        return True
                                if (self.table[self.h2.__call__(new_entry.get_key())] == None):
                                        self.table[self.h2.__call__(new_entry.get_key())] = new_entry
                                        self.added_elements.append(new_entry)
                                        return True
                                if (self.table[self.h2.__call__(new_entry.get_key())] != None and self.table[self.h2.__call__(new_entry.get_key())].get_key() == new_entry.get_key()):
                                        self.table[self.h2.__call__(new_entry.get_key())] = new_entry
                                        self.added_elements.append(new_entry)
                                        return True
                                original_element = self.table[self.h1.__call__(new_entry.get_key())]
                                if (self.table[self.h1.__call__(original_element.get_key())].get_key() == original_element.get_key()):
                                        i=2
                                elif (self.table[self.h2.__call__(original_element.get_key())].get_key() == original_element.get_key()):
                                        i=1
                                self.table[self.h1.__call__(new_entry.get_key())] = new_entry
                                new_entry = original_element
                                # if (self.table[self.h1.__call__(new_entry.get_key())] == None):
                                #         self.table[self.h1.__call__(new_entry.get_key())] = new_entry
                                #         return True
                                if (self.table[self.h1.__call__(new_entry.get_key())] == None):
                                        self.table[self.h1.__call__(new_entry.get_key())] = new_entry
                                        self.added_elements.append(new_entry)
                                        return True
                                if (self.table[self.h2.__call__(new_entry.get_key())] == None):
                                        self.table[self.h2.__call__(new_entry.get_key())] = new_entry
                                        self.added_elements.append(new_entry)
                                        return True
                                
                                        
                                #tr_value = str(new_entry.get_value())
                                #print ("eviction with i = 1. Value " + str_value + " being moved")
                                
                        elif (i == 2):
                                #str_value = str(new_entry.get_value())
                                #print ("value " + str_value + " being inserted.")
                                if (self.table[self.h2.__call__(new_entry.get_key())] == None):
                                        #print ("eviction finished at i=2")
                                        self.table[self.h2.__call__(new_entry.get_key())] = new_entry
                                        self.added_elements.append(new_entry)
                                        return True
                                if (self.table[self.h2.__call__(new_entry.get_key())] != None and self.table[self.h2.__call__(new_entry.get_key())].get_key() == new_entry.get_key()):
                                        self.table[self.h2.__call__(new_entry.get_key())] = new_entry
                                        self.added_elements.append(new_entry)
                                        return True
                                if (self.table[self.h1.__call__(new_entry.get_key())] == None):
                                        #print ("eviction finished at i=2")
                                        self.table[self.h1.__call__(new_entry.get_key())] = new_entry
                                        self.added_elements.append(new_entry)
                                        return True
                                if (self.table[self.h1.__call__(new_entry.get_key())] != None and self.table[self.h1.__call__(new_entry.get_key())].get_key() == new_entry.get_key()):
                                        #print ("condition 2")
                                        self.table[self.h1.__call__(new_entry.get_key())] = new_entry
                                        self.added_elements.append(new_entry)
                                        return True
                                original_element = self.table[self.h2.__call__(new_entry.get_key())]
                                if (self.table[self.h1.__call__(original_element.get_key())].get_key() == original_element.get_key()):
                                        i=2
                                elif (self.table[self.h2.__call__(original_element.get_key())].get_key() == original_element.get_key()):
                                        i=1
                                self.table[self.h2.__call__(new_entry.get_key())] = new_entry
                                new_entry = original_element
                                if (self.table[self.h1.__call__(new_entry.get_key())] == None):
                                        self.table[self.h1.__call__(new_entry.get_key())] = new_entry
                                        self.added_elements.append(new_entry)
                                        return True
                                if (self.table[self.h2.__call__(new_entry.get_key())] == None):
                                        self.table[self.h2.__call__(new_entry.get_key())] = new_entry
                                        self.added_elements.append(new_entry)
                                        return True
                
                                #str_value = str(new_entry.get_value())
                                #print ("eviction with i = 2. Value " + str_value + " being moved")
                                
                        counter+=1
                        if (counter == self.size):
                                break
                self.table = self.reset()
                return False
        def reset(self):
                for i in range(0,self.size):
                        self.table[i] = None
                for i in range(0,len(self.added_elements)):
                        self.put(self.added_elements[i].get_key(),self.added_elements[i].get_value())
                return self.table
        def get(self, key):
                """
                Get the element with the key from the table
                :param key: The key of the element to fetch
                :return: The value to return OR -1 if not found.
                """
                # TODO get the *value* from the element with the matching key.
                if (self.table[self.h1.__call__(key)] != None and self.table[self.h1.__call__(key)].get_key() == key):
                        return self.table[self.h1.__call__(key)].get_value()
                if (self.table[self.h2.__call__(key)] != None and self.table[self.h2.__call__(key)].get_key() == key):
                        return self.table[self.h2.__call__(key)].get_value() 
                return -1

        def remove(self, key):
                """
                Remove the element from the table.
                :param key: The key of the element to remove.
                :return: The VALUE associated to the entry that was removed.
                    -1 if the entry could not be found
                """
                # TODO remove the entry from the table with matching key and return the value.
                if (self.table[self.h1.__call__(key)] != None and self.table[self.h1.__call__(key)].get_key() == key):
                        value = self.table[self.h1.__call__(key)].get_value()
                        self.table[self.h1.__call__(key)] = None
                        return value
                if (self.table[self.h2.__call__(key)] != None and self.table[self.h2.__call__(key)].get_key() == key):
                        value = self.table[self.h2.__call__(key)].get_value()
                        self.table[self.h2.__call__(key)] = None
                        return value
                return -1

	
	
####################
# This method is not tested
# Please use to run and test
####################

def main():
        print("RUNNING MAIN")
        prng_1 = linear_hash.PseudoRandomGenerator()
        prng_2 = linear_hash.PseudoRandomGenerator(9)
        t = CuckooHashTable(10,prng_1,prng_2)
        t.put(0,10)
        t.put(1,3)
        print ("Cuckoo Hash Table:")
        print (t)
        # print ("--h1--")
        # for i in range(0,100):
        #         print (t.h1.__call__(i))
        # print ("--h2--")
        # for i in range(0,100):
        #         print (t.h2.__call__(i))

if __name__ == '__main__':
	main()
