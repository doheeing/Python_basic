a = "Letter a"

def f(a) :
    print ("A = ", a)
    
def g():
    a = 7
    f(a + 1)
    print ("A = ", a)

print ("A =",a)
f(3.14)        
g()