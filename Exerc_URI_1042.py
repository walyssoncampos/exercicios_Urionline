valores = []

# Adicionando numeros no vetor
for i in range(3):
    valor = int(input("Digite um número: "))
    valores.append(valor)

# Números em ordem crescente
valores_ordenados = sorted(valores)

for val in valores_ordenados:
    print(val)

print ("")

for num in valores:
    print(num)

