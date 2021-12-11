import math
#Programa para compra de tinta
#h = float(input("Diga a altura do local que deseja pintar: "))
#l = float(input("Diga a largura do local que deseja pintar: "))
#a = h*l
a = float(input("Digite a area em metros quadrados: "))
litrostinta = a/3
latas = math.ceil(litrostinta/18)
dinheiro = latas*80
print("----------------------------------------------------")
print(f"A área total que você deseja pintar então é {a} m².")
print(f"Para pintar essa área você vai precisar de {latas} lata(s) de 18 L (unica que tem).")
print(f"Custo: {dinheiro} R$.")
print("----------------------------------------------------")