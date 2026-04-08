# Importa o módulo "random", que permite gerar números aleatórios
import random
# Gera um número aleatório entre 0 e 5 e armazena na variável "numero"
numero = random.randint(0,5)
# Solicita ao usuário que escolha um número de 0 a 5
# O valor digitado é convertido para inteiro usando "int"
escolha = int (input("Escolha um número de 0 a 5: "))
# Verifica se o número escolhido pelo usuário é igual ao número gerado pelo computador
if escolha == numero:
  # Executa este bloco se a condição for verdadeira (acertou)
    print("Parabéns, você acertou!")
else:
 # Executa este bloco se a condição for falsa (errou)
    print("Sinto muito, você errou.")
# Exibe qual foi o número gerado pelo computador
print("Meu numero foi:", numero)