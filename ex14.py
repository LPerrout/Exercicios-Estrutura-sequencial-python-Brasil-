#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
print("bem-vindo a cauculadora de multas para peso de pesca")
peso = float(input("Digite o peso do conteudo pescado em kg: "))
if peso > 50:
    multa = 4.00*(peso-50)
    print("----------------------------------")
    print(f"Peso de peixes: {peso}")
    print(f"Peso excedente: {peso-50}")
    print(f"A multa a pagar é de {multa} R$")
    print("----------------------------------")
else:
    print(f"Não há multa a pagar já que seus peixes pesam: {peso} kg")