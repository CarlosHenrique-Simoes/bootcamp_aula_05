notas_estudantes = [150, 142, 185, 190, 149, 171, 59, 68, 69, 70]

pontuacao_maxima = 0

for nota in notas_estudantes:
    if nota > pontuacao_maxima:
        pontuacao_maxima = nota

print(pontuacao_maxima) 