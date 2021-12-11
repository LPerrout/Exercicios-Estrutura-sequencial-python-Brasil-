import math
#Programa para compra de tinta
#h = float(input("Diga a altura do local que deseja pintar: "))
#l = float(input("Diga a largura do local que deseja pintar: "))
#a = h*l
a = float(input("Digite a area em metros quadrados: "))
litrostinta1 = a/6
latas1 = math.ceil(litrostinta1/18)
dinheiro1 = latas1*80
print("----------------------------------------------------")
print(f"A área total que você deseja pintar então é {a} m².")
print(f"Para pintar essa área você vai precisar de {latas1} lata(s) de 18 L (unica que tem).")
print(f"Custo: {dinheiro1} R$.")
print("----------------------------------------------------")
print("OU")
litrostinta1 = a/6
latas1 = math.ceil(litrostinta1/3.6)
dinheiro1 = latas1*25
print("----------------------------------------------------")
print(f"A área total que você deseja pintar então é {a} m².")
print(f"Para pintar essa área você vai precisar de {latas1} lata(s) de 3,6 L (unica que tem).")
print(f"Custo: {dinheiro1} R$.")
print("----------------------------------------------------")