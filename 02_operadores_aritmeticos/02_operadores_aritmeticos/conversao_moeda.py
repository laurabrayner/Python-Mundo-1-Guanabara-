# Solicita o nome do usuário
nome = (input("Qual seu nome? "))
# Solicita o valor em reais
reais = float (input("Quantos reais você tem na carteira? "))
# Define a cotação do dólar
cotacao_dolar = 5.24
# Calcula quantos dólares podem ser comprados
dolares = reais / cotacao_dolar
# Exibe as informações
print (f"Bom dia, {nome}, bem-vindo(a) a Labor Cambio, \na cotação do dólar hoje, 30/03/2026, é {cotacao_dolar} ") 
print (f"Com essa quantia em reais, {reais}, você consegue comprar {dolares:.2f} dólares")