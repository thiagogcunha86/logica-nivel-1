#10 - problema: escreva um software informe a média aritimética de um aluno que cursou 4 bimestres

#Obtem 4 notas do aluno
nota1 = float(input("Digite a nota do 1º bimestre: "))
nota2 = float(input("Digite a nota do 2º bimestre: "))
nota3 = float(input("Digite a nota do 3º bimestre: "))
nota4 = float(input("Digite a nota do 4º bimestre: "))

# Calculo da Média
media = (nota1 + nota2 + nota3 + nota4) / 4

# Impressão da Média
print(f"A média aritmética do aluno é: {media:.2f}")
