TalkDictionary = {"おはよう":"おはよう！", "調子はどう?":"最近大変だけど、元気だよ",
"こんにちは":"こんにちは", "こんばんわ":"こんばんわ", "趣味はある？":"貴方と話をすることだね",
"調子はどう？":"最近大変だけど、元気だよ", "趣味はある?":"貴方と話をすることだね",
"今何時？":"右上見ろ？", "進捗どうですか？":"ないです",
"さようなら":"さようなら\nPythonBotSystem >>チャットボットを終了します"}


def talk_condition(cmd, TalkDic):
    CmdValCheck = cmd in TalkDic
    if CmdValCheck == False:
        print("PythonBot >>すみません、よくわかりません")
        return 1
    elif cmd == "さようなら":
        print("PythonBot >>{}".format(TalkDic[cmd]))
        return 0
    elif cmd != "さようなら":
        print("PythonBot >>{}".format(TalkDic[cmd]))
        return 1


print("PythonBotSystem >>チャットボットを起動します")
while(True):
    command = input("入力してください >>")
    talk_result = talk_condition(command, TalkDictionary)
    if talk_result == 0:
        break
    else:
        continue
