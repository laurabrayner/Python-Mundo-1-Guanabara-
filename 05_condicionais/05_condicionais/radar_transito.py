# Solicita ao usuário a velocidade do carro em KM/h
# O valor digitado é convertido para número decimal usando 'float'
velocidade = float (input("Qual a velocidade do carro em KM/h? "))
# Verifica se a velocidade ultrapassou o limite permitido (80 KM/h)
if velocidade > 80: 
  # Executa este bloco se a condição for verdadeira (estava acima da velocidade)
  # Se a velocidade for maior que 80, será cobrado R$7 por cada KM acima do limite
    multa = (velocidade-80)*7 
    print ("Você foi multado, a multa é de R$", multa)
else:
    # Executa este bloco se a condição for falsa (estava dentro do limite)
    print ("Pode seguir!")
