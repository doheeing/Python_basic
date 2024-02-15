#파일을 열어서 그 파일에서 가장 많이 나온 단어를 세는 파일


fhand = open("C:\\Dohee\\develop\\Python_basic\\new.txt")


counts = dict ()


for line in fhand :
    words = line.split()
    for word in words :
         counts[word] : counts.get(word, 0) + 1
    
##print (words)


bigword = None
bigcount = None
for word,counts in counts.items() :
    if bigcount > None or count > bigcount :
        bigword = word
        bidcount = count
        
print (bigword, bigcount)