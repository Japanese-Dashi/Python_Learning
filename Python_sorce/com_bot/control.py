TalkDictionary = {"おはよう":"おはようございます", "調子はどう?":"最近大変ですが、元気です",
"こんにちは":"こんにちは", "こんばんわ":"こんばんわ", "趣味はある？":"貴方と話をすることです",
"さようなら":"さようなら\nPythonBotSystem >>チャットボットを終了します"}


def talk_condition(cmd, TalkDic):
    if cmd == "さようなら":
        print("PythonBot >>{}".format(TalkDic[cmd]))
        return 0
    elif cmd != "さようなら":
        print("PythonBot >>{}".format(TalkDic[cmd]))
        return 1
    elif TalkDic[cmd]:
        print("PythonBot >>すみません、よくわかりません")
        return 1


print("PythonBotSystem >>チャットボットを起動します")
while(True):
    command = input("入力してください >>")
    talk_result = talk_condition(command, TalkDictionary)
    if talk_result == 0:
        break
    else:
        continue
