n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
n3 = float(input("Digite sua terceira nota: "))
n4 = float(input("Digite sua quarta nota: "))

media = ((n1*2)+ (n2*3) + (n3*4) + (n4*1))/( 2 + 3 + 4 + 1)

if(media >= 7.0):
    print("Media: %0.1f" % (media))
    print("Aluno aprovado.")
     
if(media < 5):
    print("Media: %0.1f" % (media))
    print("Aluno Reprovado.")

elif(media >= 5 and media <= 6.9):
    print("Media: %0.1f" % (media))
    print("Aluno em Exame.")
    nota_exame = float(input("Digite sua nota do exame: "))
    print("Nota do exame: %0.1f" %(nota_exame))

    media_final = (nota_exame + media)/2

    if(media_final >= 5):
        print("Aluno Aprovado.") 
        print("Media final: %0.1f" % (media_final))

    else:
        print("Aluno reprovado.")
        print("Media final: %0.1f" % (media_final))