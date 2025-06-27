import math

x1 = float(input("Digite o valor de x1: "))
y1 = float(input("\nDigite o valor de y1: "))
x2 = float(input("\nDigite o valor de x2: "))
y2 = float(input("\nDigite o valor de y2: "))

valor = (pow((x2-x1),2) + pow((y2-y1),2))
distancia = math.sqrt(valor)

print("Resultado = %0.4f" % (distancia))