# Solicita ao usuário que digite um número inteiro
numero = int (input("Fale um número: "))
# Calcula o resto da divisão do número por 2
# O operador '%' retorna o resto da divisão (módulo)
calculo = (numero % 2)
# Verifica se o resto da divisão é igual a 0
# Se for, significa que o número é par
if calculo == 0:
    print ("Seu número é par.")
else:
    # Se o resto for diferente de 0, o número é ímpar
    print ("Seu número é ímpar")
