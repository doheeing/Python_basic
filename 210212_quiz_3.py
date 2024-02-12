#ty/except를 사용해 숫자가 아닌 입력값을 받는 급여 계산 프로그램으로 수정

hours = input("일한 시간 : ")
rate = input("시급 : ")


## try 1개 아래 h 와 r을 정의하는 문장을 넣었으면 훨씬 짧은 코드로 작성 가능
try : 
    h = float(hours)
except :
    print ("Error, please enter numeric input")
    quit()
    
try :
    r = float(rate)
except :
    print ("error")
    quit()



if (0 < h <= 40) :
    pay = (h * r)
else :
    pay = ((h-40)*(r*1.5))+(40*r)

    
print ('급여 : ', pay)
