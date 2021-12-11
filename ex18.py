#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
v = float(input("Digite a velocidade da sua internet em Mbps: "))
d = float(input("Digite o tamanho do arquivo que deseja baixar em Mb: "))
t = d/v
print("Seu arquivo será baixado em {:.2} segundos ou {:.2} minutos ou {:.2} horas".format(t, t/60, t/3600))