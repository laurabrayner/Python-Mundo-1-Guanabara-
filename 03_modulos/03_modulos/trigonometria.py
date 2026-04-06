# Importa o módulo math
import math 
# Solicita o valor do ângulo em graus
ang = int (input("Digite o valor do angulo: "))
# Converte o ângulo para radianos
radianos = math.radians(ang)
# Calcula as funções trigonométricas
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)
print (f"O seno de {ang} é {seno},o cosseno é {cosseno} e a tangente é {tangente}")