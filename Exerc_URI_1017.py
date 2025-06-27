tempo = int(input("Digite o tempo gasto na viagem em horas: "))
velocidade = int(input("\nDigite o valor da velocidade média: "))

distancia = velocidade * tempo
calculo_quilometroPorLitro= (distancia/12)

print("Resultado = %0.3f" % (calculo_quilometroPorLitro))