A = int(input("Digite um valor: "))
B = int(input("Digite um valor: "))
C = int(input("Digite um valor: "))
D = int(input("Digite um valor: "))

soma_C_D = C + D
soma_A_B = A + B

if (B > C and D > A and 
    soma_C_D > soma_A_B and 
    C > 0 and D > 0 and A % 2 == 0):
    print("Valores aceitos")

else:
    print("Valores não aceitos")
