salario = float(input("Digite o valor do salario: "))
novo_salario = 0
reajuste = 0

if((salario >= 0) and (salario <= 400)):
    novo_salario = salario + (salario * 0.15)
    reajuste = novo_salario - salario
    print("Novo salario: %0.2f" % (novo_salario))
    print("Reajuste ganho: %0.2f" % (reajuste))
    print("Em percentual: 15 %")

elif((salario >= 400.01) and (salario <= 800)):
    novo_salario = salario + (salario * 0.12)
    reajuste = novo_salario - salario
    print("Novo salario: %0.2f" % (novo_salario))
    print("Reajuste ganho: %0.2f" % (reajuste))
    print("Em percentual: 12 %")

elif((salario >= 800.01) and (salario <= 1200)):
    novo_salario = salario + (salario * 0.1)
    reajuste = novo_salario - salario
    print("Novo salario: %0.2f" % (novo_salario))
    print("Reajuste ganho: %0.2f" % (reajuste))
    print("Em percentual: 10 %")

elif((salario >= 1200.01) and (salario <= 2000)):
    novo_salario = salario + (salario * 0.07)
    reajuste = novo_salario - salario
    print("Novo salario: %0.2f" % (novo_salario))
    print("Reajuste ganho: %0.2f" % (reajuste))
    print("Em percentual: 7 %")

else:
     novo_salario = salario + (salario * 0.04)
     reajuste = novo_salario - salario
     print("Novo salario: %0.2f" % (novo_salario))
     print("Reajuste ganho: %0.2f" % (reajuste))
     print("Em percentual: 4 %")