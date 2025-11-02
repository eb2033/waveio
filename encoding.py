from enum import IntEnum
import numpy as np

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

def decode(self, frames):
        match self:
            case PCMEncoding.UNSIGNED_8:
                return np.frombuffer(frames, "u1") / self.max * 2 - 1
            case PCMEncoding.SIGNED_16:
            case PCMEncoding.SIGNED_24:   
            case PCMEncoding.SIGNED_32:  
            case _:
                raise TypeError("unsupported encoding")
