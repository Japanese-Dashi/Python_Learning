print("bytesとstrの違いの検証")

# bytesの場合
bytesSen = b'\x68\x65\x6c\x6c\x6f'
'''
    bytesはバイト型(strとは型が違う)、文字コードをバイトデータに変換可能
    ASCIIコードで文字を記述できる
'''
print(list(bytesSen))
print("'bytesSen' :",type(bytesSen))
print("'bytesSen' =",bytesSen)

sample = "Shioriko Mihune"
sam_utf8 = sample.encode("utf-8")
print(sam_utf8)

# strの場合
strSen = '\u00E0 props'
print(list(strSen))
print("'strSen' :",type(strSen))
print("'strSen' :",strSen)

print("-----------------------------------------------------\n")

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value

prt_zy = to_str(b'Zeke Yeager')
repr_prt_zy = repr(to_str(b'Zeke Yeager'))

print(prt_zy)
print(repr_prt_zy)
