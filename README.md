# cuckoo-hashing
This program implements a map using a variant of cuckoo hashing that uses a single array $A$ of a given length $M$.

As in standard cuckoo hashing it uses two hash functions $h_1$: $K \rightarrow [0, \ldots, M-1]$ and $h_2:K→[0,…,M−1]$. Every item $(k, v)$ is stored either at $A[h_1(k)]$ or $A[h_2(k)]$. If both positions are full, we start an eviction sequence at $A[h_1(k)]$. If the eviction sequence does not cycle, then place the item at $A[h_1(k)]$ and return True. Otherwise, if the eviction sequence cycles, do not do anything to the table and return False.

## How to run the program?
run `python3 cuckoo_hash_table.py` to run the algorithm. You can also modify the hash table using the `main` method of `cuckoo_hash_table.py`.