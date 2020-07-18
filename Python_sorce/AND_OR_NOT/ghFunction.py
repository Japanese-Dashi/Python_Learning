def pand(pai1, pai2):
    if pai1 == pai2 and pai1 == 0:
        bunsyo1 = '''Input Number: {}, {}      Output Number: {}'''
        sentence1 = bunsyo1.format(pai1, pai2, 0)
        return sentence1
    
    else:
        bunsyo2 = '''Input Number: {}, {}      Output Number: {}'''
        sentence2 = bunsyo2.format(pai1, pai2, 1)
        return sentence2

def por(poi1, poi2):
    if poi1 == poi2 and poi1 == 1:
        bun1 = '''Input Number: {}, {}      Output Number: {}'''
        stc1 = bun1.format(poi1, poi2, 1)
        return stc1
    
    else:
        bun2 = '''Input Number: {}, {}      Output Number: {}'''
        stc2 = bun2.format(poi1, poi2, 0)
        return stc2

def pnot(pni):
    if pni == 0:
        bun = '''Input Number: {}      Output Number: {}'''
        stc = bun.format(pni, 1)
        return stc
    
    else:
        bunsyo = '''Input Number: {}      Output_Number: {}'''
        sentence = bunsyo.format(pni, 0)
        return sentence

