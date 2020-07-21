#パーセプトロンを用いた簡単なXOR回路の実装

import pyand
import pynand
import pyor

def XOR(x1, x2):
    s1 = pynand.NAND(x1, x2)
    s2 = pyor.OR(x1, x2)

    y = pyand.AND(s1, s2)
    return y
