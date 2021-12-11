#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
salporhora = float(input("Digite quanto você recebe por hora em reais: "))
horas = float(input("Digite suas horas trabalhadas no mês que deseja saber: "))
print(f"Você recebendo {salporhora} R$ e trabalhando o total {horas} horas este mês, vai receber: {horas*salporhora} R$.")