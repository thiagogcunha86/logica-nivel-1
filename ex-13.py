#13 - Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.
# Solicita ao usuário a idade em anos, meses e dias
anos = int(input("Digite a idade em anos: "))
meses = int(input("Digite a idade em meses: "))
dias = int(input("Digite a idade em dias: "))

# Converte tudo para dias
idade_em_dias = (anos * 365) + (meses * 30) + dias

# Exibe o resultado
print(f"A idade total em dias é: {idade_em_dias}")
