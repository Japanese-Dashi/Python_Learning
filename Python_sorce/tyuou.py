from statistics import median as dia

sample_list = [92, 107, 121, 159, 192, 222, 254]
nanika_list = [103, 118, 141, 178, 201, 239, 294]

print("sample_list =", sample_list)
print("nanika_list =", nanika_list)

ans1 = dia(sample_list)
ans2 = dia(nanika_list)

bun = '''sample_listの平均値: {}
nanika_listの平均値: {}'''
sentence = bun.format(ans1, ans2)

print(sentence)

input('type to exit')