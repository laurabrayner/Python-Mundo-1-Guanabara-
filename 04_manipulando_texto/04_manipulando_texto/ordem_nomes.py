# Recebe o nome e o sobrenome
nome=(input("Digite seu nome e sobrenome: ").strip().split())
# Devolve o nome
print("Seu nome é:", nome[0])
# Devolve o último sobrenome
print("Seu sobrenome é:", nome[(len(nome) - 1)])
