"""
GLib Psuedo Random Generator

======================
MAGIC NUMBERS WARNING!
A, B = MAGIC NUMBERS!!
Note: These numbers were chosen.
======================
"""


class PseudoRandomGenerator:

        # The A parameter in the pseudo random number generator.
        a = 1103515245
        # The B parameter in the pseudo random number generator.
        b = 12345

        def __init__(self, seed=1804289383):
                """
                Initialises the PRNG with the given seed or default.
                :param seed: The seed for the PRNG.
                """
                self.previous = seed
                self.base = 2**32

        def generate(self, limit=None):
                """
                Generates the next random number in the sequence.
                :param limit: The limit of the generator?
                :return: The number generated from random.
                """
                self.previous = (self.a * self.previous + self.b) % self.base;

                return self.previous

################################################################################
#
# NOTE: The main function below is to show functionality and is not used
# for testing. It can be used to understand the generated numbers.
#
################################################################################


if __name__ == '__main__':
    G = PseudoRandomGenerator(1234567896)
    print(G.generate())
    print(G.generate())
    print(G.generate())
    print(G.generate())
    print(G.generate())
    print(G.generate())
    print(G.generate())
