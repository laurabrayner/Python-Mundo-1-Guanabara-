# Solicita a largura da parede em metros
largura = float (input("Qual a largura da parede em metros? "))
# Solicita a altura da parede em metros
altura = float (input("Qual a altura da parede em metros? "))
# Calcula a área da parede
area = largura * altura
# Calcula a quantidade de tinta necessária
# Considerando que 1 litro de tinta pinta 2 metros quadrados
tinta = area / 2
# Exibe os resultados
print (f"A área da parede é {area} e a quantidade de tinta necessária pra pintar a parede é de {tinta} litros")