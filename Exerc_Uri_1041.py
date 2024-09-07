x = float(input("Digite o valor de X: "))
y = float(input("Digite o valor de Y: "))

if(x == 0 and y == 0):
    print("Origem")

elif (y == 0 ):
    print("Eixo X")

elif(x == 0):
    print("Eixo Y")

if( x > 0 and y > 0):
    print("1° Quadrante")

if(x < 0 and y > 0):
    print("2° Quadrante")

if(x < 0 and y < 0):
    print("3° Quadrante")

if(x > 0 and y < 0):
    print("4° Quadrante")