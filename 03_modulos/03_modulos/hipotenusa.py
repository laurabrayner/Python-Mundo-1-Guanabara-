# Importa o módulo math
import math
# Solicita o valor do cateto oposto
cateto_oposto = float (input("Digite o valor do cateto oposto: "))
# Solicita o valor do cateto adjacente
cateto_adjacente = float (input("Digite o valor do cateto adjacente: ")) 
# Calcula a hipotenusa usando o Teorema de Pitágoras
hipotenusa = math.sqrt(math.pow(cateto_oposto, 2) + math.pow(cateto_adjacente, 2))
# Exibe o resultado
print (f"O valor da hipotenusa é {hipotenusa:.2f}")