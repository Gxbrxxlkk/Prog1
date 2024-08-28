mult = [[0 for _ in range(3)] for _ in range(10)]

for i in range(10):
    for j in range(3):
        mult[i][j] = (i*j)
for linha in mult:
    print(linha)


def gpt1():
        # Criando uma matriz 2x3 (2 linhas, 3 colunas)
    matriz = [
        [1, 2, 3],  # Primeira linha
        [4, 5, 6]   # Segunda linha
    ]

    # Acessando um elemento (linha 1, coluna 2)
    elemento = matriz[0][1]  # Resulta em 2

    # Exibindo a matriz
    for linha in matriz:
        print(linha)

