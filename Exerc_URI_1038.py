print("-" * 50)
print(f"{'CODIGO':10} {'ESPECIFICAÇAO':20} {'PREÇO':20}")
print("-" * 50)
print(f"{'1':10} {'Cachorro Quente':20} R$ {4.00:>7.2f}")
print(f"{'2':10} {'X-Salada':20} R$ {4.50:>7.2f}")
print(f"{'3':10} {'X-Bacon':20} R$ {5.00:>7.2f}")
print(f"{'4':10} {'Torrada Simples':20} R$ {2.00:>7.2f}")
print(f"{'5':10} {'Refrigerante':20} R$ {1.50:>7.2f}")

codigo = int(input("\nDigite o código do produto desejado: "))

if(codigo != 0):
    quant = int(input("\nDigite a quantidade desejada: "))

    i = 0
    total = 0

    if(codigo == 1):
        preco = 4
        total = (preco * quant)
        print("Total: R$ %0.2f" %(total))

    if(codigo == 2):
        preco = 4.50
        total = (preco * quant)
        print("Total: R$ %0.2f" %(total))

    if(codigo == 3):
        preco = 5
        total = (preco * quant)
        print("Total: R$ %0.2f" %(total))

    if(codigo == 4):
        preco = 2
        total = (preco * quant)
        print("Total: R$ %0.2f" %(total))

    if(codigo == 5):
        preco = 1.50
        total = (preco * quant)
        print("Total: R$ %0.2f" %(total))

else:
    print("Seção Encerrada!!")


