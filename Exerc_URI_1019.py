valor = int(input("Digite o tempo de duração em segundos: "))

calculo_horas = (valor//3600)
valor = (valor % 3600)
calculo_minutos = (valor//60)
calculo_segundos = (valor % 60)

print(f"{calculo_horas}:{calculo_minutos}:{calculo_segundos}")
