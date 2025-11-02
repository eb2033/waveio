from enum import IntEnum

class PCMEncoding(IntEnum):
    UNSIGNED_8 = 1
    SIGNED_16 = 2
    SIGNED_24 = 3
    SIGNED_32 = 4

@property
    def max(self):
        return 255 if self == 1 else -self.min - 1

    @property
    def min(self):
        return 0 if self == 1 else -(2 ** (self.num_bits - 1))

    @property
    def num_bits(self):
        return 8 * self
