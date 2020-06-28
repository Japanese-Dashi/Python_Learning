import ghFunction
import ghNum

while 1:
    print("1:AND回路  2:OR回路  3:NOT回路  0:終了\n以上の中から使用したい機能を入力してください")
    kinou = input("使用したい機能の値を入力してください >> ")
    func_number = int(kinou)
    action = ghNum.actionFunc(func_number)
    #入力した値が0~3の間にあるか判定

    if action == 1:
        print("\nAND回路を実行します")
        kazu1 = input("1つ目の値を入力してください >> ")
        Num1 = int(kazu1)
        num1 = ghNum.numFunc(Num1)
        #入力した値が0, 1であるか判定

        kazu2 = input("2つ目の値を入力してください >> ")
        Num2 = int(kazu2)
        num2 = ghNum.numFunc(Num2)
        #入力した値が0, 1であるか判定

        and_answer = ghFunction.pand(num1, num2)
        print(and_answer,"\n")

    elif action == 2:
        print("\nOR回路を実行します")
        kazu3 = input("1つ目の値を入力してください >> ")
        Num3 = int(kazu3)
        num3 = ghNum.numFunc(Num3)
        #入力した値が0, 1であるか判定

        kazu4 = input("2つ目の値を入力してください >> ")
        Num4 = int(kazu4)
        num4 = ghNum.numFunc(Num4)
        #入力した値が0, 1であるか判定

        or_answer = ghFunction.por(num3, num4)
        print(or_answer, "\n")

    elif action == 3:
        print("\nNOT回路を実行します")
        suji = input("値を入力してください << ")
        Number = int(suji)
        number = ghNum.numFunc(Number)
        #入力した値が0, 1であるか判定

        not_answer = ghFunction.pnot(number)
        print(not_answer,"\n")

    elif action == 0:
        #機能を終了させるため、ループを抜けるbreakを実行
        break
