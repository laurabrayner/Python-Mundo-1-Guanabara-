# Importa o módulo random
import random
# Solicita os nomes dos alunos
aluno1 = str (input("Digite o nome do primeiro aluno: "))
aluno2 = str (input("Digite o nome do segundo aluno: "))
aluno3 = str (input("Digite o nome do terceiro aluno: "))
aluno4 = str (input("Digite o nome do quarto aluno: "))
# Cria uma lista com os nomes
lista_alunos = [aluno1, aluno2, aluno3, aluno4]
# Embaralha a ordem da lista
random.shuffle(lista_alunos)
# Exibe a nova ordem de apresentação
print (f"A ordem de apresentação é: ")
print (lista_alunos) 