import pyand
import pynand

print("AND回路とNAND回路を実装・動作させる\nまずはAND回路から")

in1, in2, cnt = 0, 0, 0
while cnt<4:
    if cnt == 0:
        ans_and1 = pyand.AND(in1, in2)
        bun = '''Input: {}, {}     Output: {}'''
        stc = bun.format(in1, in2, ans_and1)
        print(stc)

    elif cnt == 1:
        in1, in2 = 0, 1
        ans_and2 = pyand.AND(in1, in2)
        bun2 = '''Input: {}, {}     Output: {}'''
        stc2 = bun2.format(in1, in2, ans_and2)
        print(stc2)
    
    elif cnt == 2:
        in1, in2 = 1, 0
        ans_and3 = pyand.AND(in1, in2)
        bun3 = '''Input: {}, {}     Output: {}'''
        stc3 = bun3.format(in1, in2, ans_and3)
        print(stc3)
    
    elif cnt == 3:
        in1, in2 = 1, 1
        ans_and4 = pyand.AND(in1, in2)
        bun4 = '''Input: {}, {}     Output: {}'''
        stc4 = bun4.format(in1, in2, ans_and4)
        print(stc4)

    cnt += 1


print("\n次はNAND回路を動作させる。")
print('Input: 0, 0     Output: {}'.format(pynand.NAND(0, 0)))
print('Input: 0, 1     Output: {}'.format(pynand.NAND(0, 1)))
print('Input: 1, 0     Output: {}'.format(pynand.NAND(1, 0)))
print('Input: 1, 1     Output: {}'.format(pynand.NAND(1, 1)))


input('type to exit')