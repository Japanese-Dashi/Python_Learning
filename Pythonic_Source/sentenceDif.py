print("bytesとstrの違いの検証")

# bytesの場合
bytesSen = b'\x68\x65\x6c\x6c\x6f'
'''
    bytesはバイト型(strとは型が違う)、文字コードをバイトデータに変換可能
    ASCIIコードで文字を記述できる
'''
print("変数のリスト: {}, {}, 変数の中身: {}".format(list(bytesSen), type(bytesSen), bytesSen))
# list(bytesSen)では、生の符号なし8ビット値からなるASCIIエンコーディングで表示

# strの場合
strSen = '\u00E0 props'
print("変数のリスト: {}, {}, 変数の中身: {}".format(list(strSen), type(strSen), strSen))

# 区切ることを出力側で知らせるため、区切り表現をprint()で出力する
print("-----------------------------------------------------")


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
    # isinstance()関数を用いて、1番目に指定したデータが2番目の引数のデータ型と等しいかどうか判定し返す。
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value

repr_prt_zy = repr(to_str(b'Zeke Yeager'))
# repr()関数は、受け取った引数に''(シングルクオーテーション)を付ける関数
print(repr_prt_zy)


in_stc_data = input("何かしら文字データを入力して下さい\n<< ")
# in_stc_dataのstcはsentence(文章)の略


def to_bytes(in_stc_data):
    if isinstance(in_stc_data, str):
        encode_data = in_stc_data.encode('utf-8')
    else:
        encode_data = in_stc_data
    return encode_data    #bytesのインスタンス

print("入力したデータ: {}".format(repr(in_stc_data)))
print("エンコード後: {}".format(repr(to_bytes(in_stc_data))))


# strとbytesはお互い統合、データの比較ができる。しかし、型が同じでないとできない。
print(b'\x4b\x61\x6e\x61\x74\x61' + b'Suki')
print("Shine" < "DarkBlue")
