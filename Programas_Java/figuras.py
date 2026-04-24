#triangulo 1 
def triangulo1():
    h=5
    for i in range(1,h+1):
        print(' '*(h-i)+'*'*(2*i-1))
triangulo1()

print('------------------------')
#triangulo 2
def triangulo2():
    h=5
    for i in range(h,0,-1):
        print(' '*(h-i)+'*'*(2*i-1))
triangulo2()

print('------------------------')
#triangulo 3
def triangulo3():
    h=5
    for i in range(1,h+1):
        print(' '*(h-i)+'*'*i)
triangulo3()

print('------------------------')
#triangulo 4
def triangulo4():
    h=5
    for i in range(h,0,-1):
        print(' '*(h-i)+'*'*i)
triangulo4()