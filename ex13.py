#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7
genero = float(input("Digite qual seu genero, digite 1 (homem) ou 2 (mulher): "))
if genero == 1:
    h = float(input("Agora digite sua altura: "))
    p = (72.7*h) - 58
    print(f"Já que você é um homem, seu peso ideal é: {p} kg")
elif genero == 2:
    h = float(input("Agora digite sua altura: "))
    p = (62.1*h) - 44.7
    print(f"Já que você é uma mulher, seu peso ideal é: {p} kg")
else:
    print("Genero invalido")
