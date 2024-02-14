#파일을 읽고 원하는 값을 출력하는 함수


#파일 입력 받기
#a = input('File name :')
b = open('C:\\Dohee\\Python_basic\\new.txt')


#입력 받은 파일 속 from 으로 시작하는 문장을 대문자로 출력
#for line in b :
#  ly = line.rstrip()
#  if ly.startswith('From'):
#    print(ly.upper())
 
#입력받은 파일의 줄 세는 함수   
#count = 0
#for line in b :
#    count = count + 1
#print (count)

#입력받은 파일의 글자 수 세는 함수
inp = b.read()
print(len(inp))

#입력받은 파일의 49번째 글자까지 출력 함수
print(inp[:50])