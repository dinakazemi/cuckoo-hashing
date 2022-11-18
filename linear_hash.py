"""
Implement Linear Hash Function using a Mersene prime and a pseudorandom generator.

Make sure the range of the keys is < 2098960

Example:
uhf = LinearHashFunction(11)
[uhf(i) for i in range(11)]  -> [3, 8, 7, 6, 5, 10, 9, 8, 7, 6, 0]

"""

from PRNG import PseudoRandomGenerator


class LinearHashFunction:
        

        # Mersene prime
        PRIME = 2098960

        def __init__(self, N, png):
                """
                Initialises the hash function by generating the A and B parameters.
                :param N: The range of the hash.
                :param png: The seeded PseudoRandomNumber generator instance.
                """

                # Assert that N > 1
                assert N > 1, "Range of Hash function should be greater than 1"

                # First ensure the PNG is the correct png
                assert type(png) is PseudoRandomGenerator, "PseudoRandomGenerator was not passed in as correct argument"

                self.N = N

                # generate pseudorandom values of a until != 0
                self.a = png.generate() % LinearHashFunction.PRIME
                while self.a == 0:
                        self.a = png.generate() % LinearHashFunction.PRIME
                self.b = png.generate() % LinearHashFunction.PRIME

        def __call__(self, key):
                return ((self.a * key + self.b ) % LinearHashFunction.PRIME) % self.N
