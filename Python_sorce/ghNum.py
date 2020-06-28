def numFunc(pi):
    num = pi

    while 1:
        if num > 1 or num < 0:
            print("不適切な値です。入力し直してください。")
            kazu = input("値を入力してください << ")
            num = int(kazu)
        else:
            return num

def actionFunc(pi_action):
    number_action = pi_action

    while 1:
        if number_action < 0 or number_action > 3:
            print("不適切な値です。入力し直してください。")
            suji = input("値を入力してください << ")
            number_action = int(suji)
        else:
            return number_action
