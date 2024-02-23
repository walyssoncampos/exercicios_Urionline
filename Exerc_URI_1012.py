def area_triangulo(A, C):
    resultado = (A*C)/2
    return resultado

def area_circulo(C):
    resultado = 3.14159* (pow(C,2))
    return resultado

def area_trapezio(A, B, C):
    resultado = ((A+B)*C)/2
    return resultado

def area_quadrado(B):
    resultado = pow(B,2)
    return resultado

def area_retangulo(A, B):
    resultado = A*B
    return resultado

print("Para calcular area do triangulo digite 1 !!")
print("\nPara calcular area do circulo digite 2 !!")
print("\nPara calcular area do trapezio digite 3 !!")
print("\nPara calcular area do quadrado digite 4 !!")
print("\nPara calcular area do retangulo digite 5 !!")
print("\nDigite o número 0 para sair !!")

op = int(input(("\nDigite a operacao desejada: ")))

match op:
    case 1:
        val1 = float(input("Digite o primeiro valor: "))
        val2 = float(input("Digite o segundo valor: "))
        resultado = area_triangulo(val1, val2)
        print("TRIANGULO:  %0.3f " % (resultado))
    
    case 2:
        val1 = float(input("Digite o valor do raio: "))
        resultado = area_circulo(val1)
        print("CIRCULO:  %0.3f " % (resultado))

    case 3:
        val1 = float(input("Digite o valor da primeira base: "))
        val2 = float(input("Digite o valor d segunda base: "))
        val3 = float(input("Digite o valor da altura: "))
        resultado = area_trapezio(val1, val2, val3)
        print("TRAPEZIO:  %0.3f " % (resultado))

    case 4:
        val1 = float(input("Digite o primeiro valor: "))
        resultado = area_quadrado(val1)
        print("QUADRADO:  %0.3f " % (resultado))

    case 5:
        val1 = float(input("Digite o primeiro valor: "))
        val2 = float(input("Digite o segundo valor: "))
        resultado = area_retangulo(val1, val2)
        print("RETANGULO:  %0.3f " % (resultado))

    case 0:
        print("Voce saiu. Até mais !!")
        
    
