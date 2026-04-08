# Exibe uma mensagem informando ao usuário o que deve ser feito
print ("Preciso que você me diga três medidas.")
# Solicita a medidas e converte o valor para número inteiro
a = int (input("Medida um: "))
b = int (input("Medida dois: "))
c = int (input("Medida três: "))
# Verifica a condição de existência de um triângulo
# A soma de dois lados sempre deve ser maior que o terceiro lado
if a + b > c and a + c >b and b + c > a:
   # Executa se todas as condições forem verdadeiras
    print ("É possível formar um triângulo")
else:
    # Executa se alguma condição for falsa
    print ("Não é possível formar um triângulo")