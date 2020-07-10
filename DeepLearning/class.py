class Info:
    def __init__(self, name):
        self.name = name
        #Initialized!初期化された。


    def notice(self):
        if self.name == "Fukuda":
            Lname = input("名字だけでなく名前も入力してください << ")
            if Lname == "Koji":
                print("死ねカス!!!")
            else:
                print("人違いだったようです。\n")

        elif self.name == "Koji":
            Fname = input("名前も入力してください << ")
            if Fname == "Fukuda":
                print("授業料返すか単位をよこせ!!")
            else:
                print("ぴえん\n")

        else:
            print("Hello,",self.name+"!")


    def goodby(self):
        print("Good-by,", self.name,"\n")



input_name = input("名前を入力してください << ")

pyi = Info(input_name)
pyi.notice()
pyi.goodby()


input('type to exit')