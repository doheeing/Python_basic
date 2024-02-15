#dic 안에 있는 숫자 작은순으로 배열 후 kev-value 순서로 출력 하기

a = {'a' : 10, 'b': 1, 'c': 22}

b = sorted([(v,k) for k, v in a.items()])

for val, key in b :
    print (key, val)