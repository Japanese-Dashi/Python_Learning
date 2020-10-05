import Arithmetic_Operations as AO
import math

while 1:
    print("1: 加算  2: 減算  3: 乗算  4: 除算  5: 累乗  6: exp()  7: 奇数、偶数判定  8: 因数分解  9: 階乗  0: 終了")

    inStr = input("使用したい機能番号を入力してください << ")
    inNum = int(inStr)

    if inNum == 0:
        break
    elif inNum == 1:
        inA = input("1つ目の数字: ")
        inB = input("2つ目の数字: ")
        inC = input("3つ目の数字: ")
        inD = input("4つ目の数字: ")

        a1, b1, c1, d1 = int(inA), int(inB), int(inC), int(inD)
        plus_ans = AO.Plus(a1, b1, c1, d1)

        print("加算結果は{}です\n".format(plus_ans))
    elif inNum == 2:
        iA = input("1つ目の数字: ")
        iB = input("2つ目の数字: ")

        a2, b2 = int(iA), int(iB)
        minus_ans = AO.Minus(a2, b2)

        print("減算結果は{}です\n".format(minus_ans))
    elif inNum == 3:
        in_A = input("1つ目の数字: ")
        in_B = input("2つ目の数字: ")
        in_C = input("3つ目の数字: ")

        a3, b3, c3 = int(in_A), int(in_B), int(in_C)
        multi_ans = AO.Multi(a3, b3, c3)

        print("乗算結果は{}です\n".format(multi_ans))
    elif inNum == 4:
        input_A = input("1つ目の数字: ")
        input_B = input("2つ目の数字: ")
        input_C = input("3つ目の数字: ")

        a4, b4, c4 = int(input_A), int(input_B), int(input_C)
        division_ans = AO.Division(a4, b4, c4)

        print("除算結果は{}です\n".format(division_ans))
    elif inNum == 5:
        in1 = input("1つ目の数字: ")
        in2 = input("2つ目の数字: ")
        a5, b5 = int(in1), int(in2)

        expo_ans1 = AO.Exponentiation(a5, b5)
        expo_ans2 = AO.Exponentiation(b5, a5)

        print("{}の{}乗は{}です\n".format(a5, b5, expo_ans1))
        print("{}の{}乗は{}です\n".format(b5, a5, expo_ans2))
    elif inNum == 6:
        i1 = input("数字を入力してください: ")
        a6 = int(i1)
        print("{0}の対数関数(e^{0})は{1}です\n".format(a6 ,math.exp(a6)))
    elif inNum == 7:
        in_1 = input("数字を入力してください: ")
        a7 = int(in_1)

        ans = AO.EvenOROdd(a7)
        if ans == 0:
            ans_sen = "偶数"
        else:
            ans_sen = "奇数"

        print("{}は{}である\n".format(a7, ans_sen))
    
