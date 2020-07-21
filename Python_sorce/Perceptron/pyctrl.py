import pyand
import pynand
import pyor
import pyxor

print("AND回路、NAND回路、OR回路、XOR回路を実装・動作させる\nまずはAND回路から")
print('Input: 0, 0     Output: {}'.format(pyand.AND(0, 0)))
print('Input: 0, 1     Output: {}'.format(pyand.AND(0, 1)))
print('Input: 1, 0     Output: {}'.format(pyand.AND(1, 0)))
print('Input: 1, 1     Output: {}'.format(pyand.AND(1, 1)))


print("\n次はNAND回路を動作させる。")
print('Input: 0, 0     Output: {}'.format(pynand.NAND(0, 0)))
print('Input: 0, 1     Output: {}'.format(pynand.NAND(0, 1)))
print('Input: 1, 0     Output: {}'.format(pynand.NAND(1, 0)))
print('Input: 1, 1     Output: {}'.format(pynand.NAND(1, 1)))


print("次はOR回路を動作させる。")
print('Input: 0, 0     Output: {}'.format(pyor.OR(0, 0)))
print('Input: 0, 1     Output: {}'.format(pyor.OR(0, 1)))
print('Input: 1, 0     Output: {}'.format(pyor.OR(1, 0)))
print('Input: 1, 1     Output: {}'.format(pyor.OR(1, 1)))


print("次はXOR回路を動作させる。")
print('Input: 0, 0     Output: {}'.format(pyxor.XOR(0, 0)))
print('Input: 0, 1     Output: {}'.format(pyxor.XOR(0, 1)))
print('Input: 1, 0     Output: {}'.format(pyxor.XOR(1, 0)))
print('Input: 1, 1     Output: {}'.format(pyxor.XOR(1, 1)))


input('type to exit')