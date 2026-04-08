# Solicita ao usuário que digite um número de 0 a 9999
numero=(input("Digite um número de 0 a 9999: "))
# A variável 'numero' é uma string, então podemos acessar cada posição
# Cada posição representa um dígito do número
# Pega o último dígito (posição 3) -> Unidade
unidade=numero[3]
# Pega o terceiro dígito (posição 2) -> Dezena
dezena=numero[2]
# Pega o segundo dígito (posição 1) -> Centena
centena=numero[1]
# Pega o primeiro dígito (posição 0) -> Milhar
milhar=numero[0]
# Exibe cada parte do número separadamente
print("Unidade:", unidade, "\n" "Dezena:", dezena, "\n" "Centena:", centena, "\n" "Milhar:", milhar)

