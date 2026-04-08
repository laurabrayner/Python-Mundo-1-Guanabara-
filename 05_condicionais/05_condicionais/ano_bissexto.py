# Solicita ao usuário que digite um ano
# O valor digitado é convertido para número inteiro usando 'int'
ano = int (input("Digite o ano:"))
# Verifica se o ano é bissexto
# Regras:
# 1. O ano deve ser divisível por 4
# 2. Não pode ser divisível por 100, exceto se também for divisível por 400
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  # Executa se o ano for bissexto
    print ("O ano é bissexto!")
else:
  # Executa se o ano não for bissexto
    print ("O ano não é bissexto.")