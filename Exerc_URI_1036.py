import math

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = (pow(b,2)- 4*a*c)

if a==0 or delta < 0:
    print("Impossível resolver")

else:
    raiz = math.sqrt(delta)
    R1 = (-b + raiz)/(2*a)
    R2 = (-b - raiz)/(2*a)
    #print("R1 = {} \nR2 = {} ".format(R1, R2))
    print("R1 = %0.5f " % (R1), "\nR2 = %0.5f" % (R2))
