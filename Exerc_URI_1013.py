a = int(input("Digite o primeiro valor: "))
b = int(input("\nDigite o segundo valor: "))
c = int(input("\nDigite o terceiro valor: "))

MaiorAB =(a+b+abs(a-b))/2

if(MaiorAB < c):
    MaiorABC = c
    print(f"O maior valor eh: {MaiorABC}")

else:
    print(f"O maior valor eh: {MaiorAB}")
    