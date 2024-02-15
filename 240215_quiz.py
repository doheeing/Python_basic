#split 함수 사용


fhand = open("C:\\Dohee\\develop\\Python_basic\\new.txt")

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    words = line.split()
    email =words[1]
    a = email.split('@')
    id = a[0]
    print(id)
    