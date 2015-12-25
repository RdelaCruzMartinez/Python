a = 7
b = 4
c = 0

def resolverEq2nGrado(a,b,c):
    import math
    
    if a==0:
        return None
    if b==0 and -c/a<0:
        return None
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c) / 2 * a)
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c) / 2 * a)
    return x1, x2


#Caso Test a = 0 donde no existe solución real
if a == 0:
    if None == resolverEq2nGrado(a, b, c):
        print ("PASS a=0")
    else:
        print ("FAIL a=0")

#Caso Test b = 0 y -c/a<0 donde no existe solución real
if b == 0 and -c/a < 0:
    if None == resolverEq2nGrado(a, b, c):
       print ("PASS b=0 y -c/a<0")
    else:
       print ("FAIL b=0 y -c/a<0")
       
#Caso Test c = 0 donde x1 = 0 y x2 = -b/a
if c == 0:
    x1, x2 = resolverEq2nGrado(a, b, c)
    if x1 == 0 and x2 == -b/a:
        print ("PASS c=0")
    else:
        print ("FAIL c=0")

#Caso Test b = 0 y c = 0 donde x1 = x2 = 0
if b == 0 and c == 0:
    x1, x2 = resolverEq2nGrado(a, b, c)
    if x1 == 0 and x2 == 0:
        print ("PASS b=0, c=0")
    else:
        print ("FAIL b=0, c=0")

#fin
