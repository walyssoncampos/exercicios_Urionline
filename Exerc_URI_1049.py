palavra = input("Digite a primeira palavra: ")

if(palavra == 'vertebrado'):
    palavra2 = input("Digite a segunda palavra: ")

    if(palavra2 == 'ave'):
        palavra3 = input("Digite a terceira palavra: ")

        if(palavra3 == 'carnivoro'):
            print("aguia")

        elif(palavra3 == 'onivoro'):
            print("pomba")
        
        else:
            print("ERRO! Terceira Palavra Incorreta.")

    elif(palavra2 == 'mamifero'):
        palavra3 = input("Digite a terceira palavra: ")

        if(palavra3 == 'onivoro'):
            print("homem")

        elif(palavra3 == 'herbivoro'):
            print("vaca")

        else:
            print("ERRO! Terceira Palavra Incorreta.")

    else:
        print("ERRO! Segunda Palavra Incorreta.")

elif(palavra == 'invertebrado'):
    palavra2 = input("Digite a segunda palavra: ")

    if(palavra2 == 'inseto'):
        palavra3 = input("Digite a terceira palavra: ")

        if(palavra3 == 'hematofago'):
            print("pulga")

        elif(palavra3 == 'herbivoro'):
            print("lagarta")

        else:
            print("ERRO! Terceira palavra Incorreta")

    if(palavra2 == 'anelideo'):
        palavra3 = input("Digite a terceira palavra: ")

        if(palavra3 == 'hematofago'):
            print("sanguessuga")

        elif(palavra3 == 'onivoro'):
            print("minhoca")

        else:
            print("ERRO! Terceira palavra Incorreta")

    else:
        print("ERRO! Segunda Palavra Incorreta.")

else:
    print("ERRO! Palavra Incorreta.")
