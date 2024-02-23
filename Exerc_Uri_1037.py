
valor = float(input("Digite um valor qualquer: "))

if valor >= 0 and valor <= 25:
    print("Intervalo (0,25]")

if valor > 25 and valor <= 50:
    print("Intervalo (25,50]")

if valor > 50 and valor <= 75:
    print("Intervalor (50, 75]")

if valor > 75 and valor <= 100:
    print("Intervalo (75, 100]")

else:
    print("Fora do intervalo")

