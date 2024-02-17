#image file 을 튜플을 활용해 디지털 사진 색깔 반전 변환 

from cs1media import *

img = load_picture()

w, h = img.size() #img.size는 튜플을 리턴함

for y in range(h) : # range 함수는 괄호 안의 값 이하까지의 정수를 생성함
    for x in range(w) :
        r, g, b = img.get(x.y) #get(x,y) 함수는 x,y 좌표의 점의 RGB 값을 return 함
        r, g, b = 255 - r, 255 - g, 255 - b
        img.set(x, y,(r, g, b)) #새로 바꾼 r,g,b 값을 대입