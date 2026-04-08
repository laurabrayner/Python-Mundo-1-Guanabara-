# Solicita ao usuário o valor do salário
# O valor digitado é convertido para número decimal usando 'float'
salario = float (input("Qual o seu salário? "))
# Verifica se o salário é maior que R$1250,00
if salario > 1250.00:
  # Se for maior, recebe um aumento de 10%
    novosalario = salario*1.10
  # Exibe o novo salário com duas casas decimais
    print(f"Seu salário com aumento é:{novosalario:.2f}")
else:
    # Se for menor ou igual a R$1250,00, recebe um aumento de 15%
    novosalario = salario*1.15 
   # Exibe o novo salário com duas casas decimais
    print(f"Seu salário com aumento é:{novosalario:.2f}")