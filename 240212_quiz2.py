#40시간을 초과한 시간의 시급을 1.5배 하여 급여 계산 프로그램 만들기
#Enter Hours : 45 
#Enter Rate : 10


hours = input('일한 시간 : ')
rate = input('시급 : ')

h = float(hours)
r = float(rate)

if h <= 40 :
    pay = (h * r)
else :
    pay = ((h-40)*(r*1.5))+(40*r)
    
print ('급여 : ', pay)