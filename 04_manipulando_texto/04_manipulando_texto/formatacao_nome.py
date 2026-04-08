# Recebe o nome completo do usuário
nome=(input("Digite seu Nome e Sobrenome: "))
# Exibe o nome em letras maiúsculas
print(nome.upper())
# Exibe o nome em letras minúsculas
print(nome.lower())
# Exibe a quantidade de letras sem contar os espaços
print(len(nome.replace(" ", "")))
# Exibe a quantidade de letras do primeiro nome
print(len(nome.split()[0]))