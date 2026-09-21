# TODO: Implemente a expressão de validação
media_aluno = float(input("Nota do Aluno-"))
frequencia_percentual = int(input("Frequencia do aluno-"))

aprovado = media_aluno >= 6 and frequencia_percentual >=75
print("Status de aprovação:", aprovado)

