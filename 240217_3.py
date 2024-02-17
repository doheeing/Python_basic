#image file 을 튜플을 활용해 디지털 사진 흑백변환 

threshold = 100
white = (255, 255, 255)
black = (0, 0, 0)

img = load_picture()
w, h = img.size()
for y in range(h) :
    for x in range(w) :
        r, g, b = img.get(x, y)
        v = (r + g + b)//3
        if v > threshold :
            img.set(x, y, white)
        else :
            img.set(x, y, black)
img.show()