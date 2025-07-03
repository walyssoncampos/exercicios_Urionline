print("-" * 40)
print(f"{'DDD':10} {'Destination':20}")
print("-" * 40)
print(f"{'61':10} {'Brasilia':20}")
print(f"{'71':10} {'Salvador':20}")
print(f"{'11':10} {'Sao Paulo':20}")
print(f"{'21':10} {'Rio de Janeiro':20}")
print(f"{'32':10} {'Juiz de Fora':20}")
print(f"{'19':10} {'Campinas':20}")
print(f"{'27':10} {'Vitoria':20}")
print(f"{'31':10} {'Belo Horizonte':20}")

codigo = int(input("Digite um DDD: "))

if((codigo != 61) and (codigo != 71) and (codigo != 11) and (codigo != 21) and (codigo != 32) and (codigo != 19) and (codigo != 27) and (codigo != 31)):
    print("DDD não cadastrado")

elif(codigo == 61):
    print("Brasilia")

elif(codigo == 71):
    print("Salvador")

elif(codigo == 11):
    print("Sao Paulo")

elif(codigo == 21):
    print("Rio de Janeiro")

elif(codigo == 32):
    print("Juiz de Fora")

elif(codigo == 19):
    print("Campinas")

elif(codigo == 27):
    print("Vitoria")

elif(codigo == 31):
    print("Belo Horizonte")

