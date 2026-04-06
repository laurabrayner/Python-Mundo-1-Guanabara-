# Importa o módulo math
import math 
# Solicita um número decimal
num = float (input("Digite um número: ")) 
# Obtém a parte inteira do número
parte_inteira = math.trunc(num)
# Exibe o resultado
print (f"A parte inteira de {num} é {parte_inteira}")