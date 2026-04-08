# Solicita ao usuário a distância da viagem em quilômetros
# O valor digitado é convertido para número inteiro usando 'int'
distancia = int (input("Digite a distância da viagem em KM: "))
# Verifica se a distância é menor ou igual a 200 KM
if distancia <= 200:
   # Se a distância for até 200 KM, o preço é R$0,50 por KM
    ticket = (0.5*distancia)
    print("O valor da sua viagem é R$", ticket)
else: 
 # Se a distância for maior que 200 KM, o preço é R$0,45 por KM
    ticket = (0.45*distancia)
    print("O valor da sua viagem é R$", ticket)