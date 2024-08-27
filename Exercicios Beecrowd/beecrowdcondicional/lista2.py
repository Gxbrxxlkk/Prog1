def media():
    n1, n2, n3, n4 = map(float, input().split())

    n1 *= 2
    n2 *= 3
    n3 *= 4

    media = (n1 +n2 +n3 + n4)/10
    exame = 0
    print(f'Media: {media:.1f}')
    if media >= 7:
        print("Aluno aprovado.")
    elif media < 5:
        print("Aluno reprovado.")
    elif media >= 5 or media <= 6.9:
        print("Aluno em exame.")
        exame = float(input("Nota do exame: "))
        media = (media + exame)/2
        if media >= 5:
            print("Aluno aprovado.")
            print(f"Media final: {media:.1f}")
        else:
            print("Aluno reprovado.")
            print(f"Media final: {media:.1f}")

def cordenadas():
    X, Y = map(float, input().split())
    if(X == 0) and (Y == 0):
        print("Origem")
    elif(X<0):
        if(Y<0):
            print("Q3")
        elif(Y>0):
            print("Q2")
    elif(X>0):
        if(Y>0):
            print("Q1")
        elif(Y<0):
            print("Q4")
    elif(X ==0) and (Y != 0):
        print("Eixo X")
    elif(X != 0) and (Y == 0):
        print("Eixo Y")


def triangulo():
    valores = []
    for i in range(3):
        valores[i] = input()
    valores = valores.sort(reverse=True)
    print(valores)

triangulo()