A = float(input("Digite um valor: "))
B = float(input("Digite um valor: "))
C = float(input("Digite um valor: "))

if(B>A):
    aux = A
    A = B
    B = aux
if(C>A):
    aux = A
    A = C
    C = aux

A_quadrado = pow(A, 2)
operacao = ((B*B)+(C*C))

if(A >= (B+C)):
    print("NAO FORMA TRIANGULO")

else:
    if ((A_quadrado) > operacao):
        print("TRIANGULO OBTUSANGULO")

    elif((A_quadrado) < operacao):
        print("TRIANGULO ACUTANGULO")

    else:
        print("TRIANGULO RETANGULO")

if(A==B and B==C):
    print("TRIANGULO EQUILATERO")

elif(A==B or A==C or B==C):
    print("TRIANGULO ISOSCELES")


    


