A = float(input("Digite um valor: "))
B = float(input("Digite um valor: "))
C = float(input("Digite um valor: "))

if((A+B > C) and (A+C > B) and (B+C > A)):
    perimetro = A + B + C
    print("Perimetro = %0.1f" % (perimetro))

