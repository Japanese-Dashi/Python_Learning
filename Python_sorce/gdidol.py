idol_list = ["高坂穂乃果", "南ことり", "園田海未", "星空凛", "小泉花陽", "西木野真姫",
             "東條希", "矢澤にこ", "絢瀬絵里", "高海千歌", "渡辺曜", "桜内梨子",
             "黒澤ルビィ", "国木田花丸", "津島善子", "黒澤ダイヤ", "松浦果南", "小原鞠莉",
             "上原歩夢", "宮下愛", "優木せつ菜", "天王寺璃奈", "桜坂しずく", "中須かすみ",
             "エマ･ヴェルデ", "近江彼方", "朝香果林"]

print("相性のいいアイドルを表示します")
while True:
    in_str = input("整数を入力してください << ")
    if in_str == 'finish':
        break

    in_num = int(in_str)

    id_length = len(idol_list)

    if id_length > in_num:
        answer = id_length % in_num
    elif id_length <= in_num:
        answer = in_num % id_length

    print("貴方と相性の良いアイドル :", idol_list[answer])


input('type to exit')