

a = open("C:\\Dohee\\develop\\Python_basic\\new.txt")

counts = {}

for line in counts :
    words = line.split()
    for word in words :
        counts[word] = counts.get(word, 0) +1
        
         print counts[:]