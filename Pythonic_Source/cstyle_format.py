print("Cスタイルフォーマット文字列とstr.formatは使わずf文字列で埋め込む")

# 出力メッセージの区切りを示す関数。正直あってもなくても変わらん。
def kugiri_print():
    print("----------------------------------------------------------------------")


# valiaはvariablesの略称
varia_a = 0b11010011    # 読みにくい2進数値を格納した変数
varia_b = 0xf3b         # 16進数値を格納した変数
print('Binary is %d, Hexad is %d.' % (varia_a, varia_b))
# フォーマット指定の構文はC言語のprintf関数に由来する

kugiri_print()


# pantryは食糧庫、食料貯蔵庫という意味
pantry = [
    ('avocados', 125),
    ('bananas', 25),
    ('cherries', 150)
]
# enumerate関数は、forループの中でリスト･タプルの要素と順番を取得できる
for i, (item, count) in enumerate(pantry):
    print('#%d: %-10s = %d' % (i, item, count))

print("\n出力メッセージをもう少し見やすくする")
for i2, (item2, count2) in enumerate(pantry):
    print('#%d: %-10s = %d' % (
        i2 + 1,
        item2.title(),    # 要素のタイトルを取得
        round(count2)))   # round関数を用いて、
kugiri_print()


name = input("名前を英語表記で入力してください >>")

template = '%s loves many kinds food. See %s cook.'
before = template % (name, name)    # タプル形式でフォーマット

template = '%(name)s loves many kinds food. See %(name)s cook.'
after = template % {'name': name}    # 辞書形式でフォーマット

print("before after is equal?: {}\n{}\t{}".format(before==after, before, after))

kugiri_print()


# メニューの要素を辞書形式で作成
menu = {
    'soup': 'lentil',
    'oyster': 'Kumamoto',
    'special': 'schnitzel'
}
# %()で、カッコ内の変数を文の中にフォーマットしている
template_other = ('Today\'s soup is %(soup)s, '
                  'buy one get two %(oyster)s oysters, '
                  'and our special entree is %(special)s.')

formatted = template_other % menu
print(formatted)

kugiri_print()


# 税抜き価格を格納
base_price = 1245
# 税率が13%として、1.13をかけている
Tax_in_price = base_price * 1.13
# 税込み価格を、でフォーマットしている
prices_format = format(Tax_in_price, ',.2f')
print("ある商品について、税抜き価格{}円であり、小数点以下込みでの税込価格は{}円である。".format(base_price, prices_format))

base_sentence = 'My String'
# base_sentenceを15文字の範囲内で中央揃えになるようにフォーマット
sentence_format = format(base_sentence, '^15s')
print('*{}*'.format(sentence_format))

kugiri_print()


name_data = 'Frieda reiss'
titan_data = 'Founding Titan'
age_data = 18
print('She name is {0}. {0} has power of {1}. {0}\'s age is {2}'.format(name_data, titan_data, age_data))
