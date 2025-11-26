#36
a = {100,200,300,400,500}
b = {100,200,300,400,500}

if a.issuperset(b) and a.issubset(b):
    print('동시')
elif a.issuperset(b):
    print('상위')
elif a.issubset(b):
    print('부분')