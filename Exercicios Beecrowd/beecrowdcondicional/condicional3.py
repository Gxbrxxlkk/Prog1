def triangulo():

    A, B, C = map(float, input().split())

    valores= []
    valores.append(A)
    valores.append(B)
    valores.append(C)
    valores.sort(reverse=True)
    print(valores)
    A2 = valores[0]**2
    B2 = valores[1]**2
    C2 = valores[2]**2
    

    if (A >= (B+C)):
        print("NAO FORMA TRIANGULO")
    else: 
        if(A2 == (B2 + C2)):
            print("TRIANGULO RETANGULO")
        if (A2 > (B2 + C2)):
            print("TRIANGULO OBTUSANGULO")
        if (A2 < (B2 + C2)):
            print("TRIANGULO ACUTANGULO")
        if (A == B) and (A == C):
            print("TRIANGULO EQUILATERO")
        if ((A == B and A != C) or (B == C and B != A)):
            print("TRIANGULO ISOSCELES")

triangulo()

def tempjogo():
    

    comeco, termino = map(float, input().split())
    jogado = 0
    if comeco < termino:
        jogado = comeco - termino 
        jogado *= -1
        print(f'O JOGO DUROU {int(jogado)} HORA(S)')
    elif comeco == termino:
        jogado = 24
        print(f'O JOGO DUROU {int(jogado)} HORA(S)')
    elif comeco > termino:
        """comeco a jogar as 20 e termino as 19, quantas horas de jogo tenho? e como calulo?
                            comeco - termino, pega o resultado e subtrai por 24?"""
        jogado = comeco - termino
        jogado -= 24
        jogado *= -1
        print(f'O JOGO DUROU {int(jogado)} HORA(S)')
    
    

