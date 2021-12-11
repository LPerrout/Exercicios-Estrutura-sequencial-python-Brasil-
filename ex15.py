#calculadora de salario com descontos
print("Bem-vindo a calculadora de salarios")
salario = float(input("Digite o quanto você recebe por hora em R$: "))
horas = float(input("Digite a quantidade de horas trabalhadas: "))
salariobruto = salario*horas
ir = (11/100)*salariobruto
inss = (8/100)*salariobruto
sindicato = (5/100)*salariobruto
salarioliquido = salariobruto - ir - inss - sindicato
print("-----------------------------------------")
print(f"\t+ Salário Bruto : {salariobruto} R$")
print(f"\t- IR (11%) : {ir} R$")
print(f"\t- INSS (8%) : {inss} R$")
print(f"\t- Sindicato (5%) : {sindicato} R$")
print(f"\t= Salário Liquido : {salarioliquido} R$")
print("-----------------------------------------")