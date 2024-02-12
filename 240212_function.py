#월급 계산 프로그램
#이름이 computepay 이고 2개의 매개 변수(시간과 시급)을 받는 함수 작성하기


hour = input("근무 시간 :")
rate = input("시급 :")

h = float(hour)
r = float(rate)


def computepay(a, b) :
    if (a <=40) :
        return a*b
    if (a>40) :
        return (40*b)+(a-40)*(b*1.5)

print (computepay (h, r))