valor = int(input("Informe sua idade em dias: "))

calculo_anos = (valor//365)

valor = (valor % 365)

calculo_meses = (valor // 30)

calculo_dias = (valor % 30)


print(f"{calculo_anos} ano (s)")
print("\n")
print(f"{calculo_meses} mes (es)")
print("\n")
print(f"{calculo_dias} dia (s)")

