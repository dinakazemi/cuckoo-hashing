"""
Interface for a HashTable.

Provides the minimum hashtable interface that will be used
to put, get and remove elements from the table.
"""
import abc


class HashTableInterface(metaclass=abc.ABCMeta):

        @abc.abstractmethod
        def __init__(self, m, prng):
                """
                Initialises the table with the correct hashes.
                :param m: The size of the table.
                :param h1n: The first variant of the hash.
                :param h2n:  The second variant of the hash.
                :param prng: The Seeded Pseudo Random Number Generator.
                """

                pass

        @abc.abstractmethod
        def put(self, k, v):
                """
                Puts the value into an entry into the table.
                :param k: The key for the matching value.
                :param v: The value to place into the table.
                """
                pass

        @abc.abstractmethod
        def get(self, key):
                """
                Get the element with the key from the table
                :param key: The key of the element to fetch
                :return: The value to return OR -1 if not found
                """
                pass

        @abc.abstractmethod
        def remove(self, key):
                """
                Remove the element from the table.
                :param key: The key of the element to remove.
                :return: The VALUE associated to the entry that was removed.
                   OR -1 if key not found
                """
                pass
