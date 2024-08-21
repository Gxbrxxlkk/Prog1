"""10. Escreva um script que solicite três números de ponto flutuante diferentes para o usuário. Em seguida, exiba os números em ordem crescente.
Lembre-se de que um conjunto de instruções if pode conter mais de uma instrução. Prove que seu script funciona executando-o em todas as seis 
ordenações possíveis dos números. Desafio extra: Seu script funciona com números duplicados?"""

numero1 = float(input("Insira seu primeiro numero real:"))
numero2 = float(input("Insira seu segundo numero real:"))
numero3 = float(input("Insira seu terceiro numero real:"))

if(numero1 < numero2) and (numero2<numero3):
    print(numero1)
    print(numero2)
    print(numero3)
elif(numero1 < numero3)and(numero3<numero2):
    print(numero1)
    print(numero3)
    print(numero2)
elif(numero3<numero1)and(numero1<numero2):
    print(numero3)
    print(numero1)
    print(numero2)
elif(numero3 < numero2) and (numero2<numero1):
    print(numero3)
    print(numero2)
    print(numero1)
elif(numero2 < numero3)and(numero3<numero1):
    print(numero2)
    print(numero3)
    print(numero1)
elif(numero2<numero1)and(numero1<numero3):
    print(numero2)
    print(numero1)
    print(numero3)
