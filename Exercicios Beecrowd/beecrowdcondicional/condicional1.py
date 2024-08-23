"""UFMT
Professor: Ivairton
ALuno: Gabriel Pivetta
Tarefas do beecrowd
"""


def pares():
    #digita os numeros pares de 0 a 100
    for pares in range(0,101, 2):
        print(pares)
    escolha()

def bhaskara():
    #Faz a bhaskara de 3 valores inserido

    valor1= input("Insira seu primeiro valor:")
    valor2= input("Insira seu segundo valor:")
    valor3= input("Insira seu terceiro valor: ")


    while valor1 != float and valor2 !=float and valor3!=float:
        print("Valores não são numeros\n")
        valor1= float(input("Insira seu primeiro valor:"))
        valor2= float(input("Insira seu segundo valor:"))
        valor3= float(input("Insira seu terceiro valor: "))


    delta = (valor2**2 -4*valor1*valor3)
    raizdelta= delta**(1/2)
    raiz1 = 0
    raiz2 = 0


    if(delta < 0):
        print("Impossivel calcular, raiz de delta é negativo")

    elif(valor1 == 0):
        print("Imposivel de calcular a Bhaskara, divisão por 0 não existe")
            
    elif(raizdelta == 0):
        
        raiz1 = ((-1*valor2) + raizdelta)/(2*valor1)
        raiz2 = ((-1*valor2) - raizdelta)/(2*valor1)

        print(f"Seu delta é igual a zero, suas raizes são: {raiz1:.5f} e {raiz2:.5f}")
    
    elif(raizdelta > 0):

        raiz1 = ((-1*valor2) + raizdelta)/(2*valor1)
        raiz2 = ((-1*valor2) - raizdelta)/(2*valor1)

        print(f"Você tem delta maior que zero, suas raizes são:\n Raiz 1 {raiz1:.5f} Raiz 2 {raiz2:.5f}")
    escolha()

def positivosemedia():
    #recebe 6 valores do usuario, diz quantos são positivos e faz a média dos positivos
    valor = 1
    qtdnumpositivos = 0
    soma = 0
    print("Insira 6 valores:")
    for i in range(6):

        valor = float(input(f"Insira seu valor {i+1}: "))
        if(valor > 0):
            soma += valor
            qtdnumpositivos += 1
        
    if(qtdnumpositivos == 0):
        print("Não terá média pois não existe valores positivos")
    else:
        media = soma/qtdnumpositivos
        print("A Quantidade de numeros positivos é:", qtdnumpositivos)
        print(f"A média entre os numeros positivos é: ", media)
    escolha()

def somadenumerosimpares():
    #Usuário vai inserir dois valores que vai gerar um intervalo entre eles e somar os numeros impares no intervalo

    valor1= int(input("Escolha o começo do seu intervalo: "))
    valor2= int(input("Escolha o fim do seu intervalo: "))
    soma = 0
    ind=0
    if (valor1 > valor2):
        valor1, valor2 = valor2, valor1
    
        
    for i in range(valor1,valor2+1):
        if i%2 != 0 and (i <0):
            soma += i
            print("Valor de i: ", i)
            print("Valor da soma atual:", soma)
        else:
            soma *= -1
            soma += i 
           
    
    print(f"A soma é: {soma}")
    escolha()
















def escolha():
    #Menu de escolha da função que quer usar
    escolha=int(input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nDigite o número da função que deseja usar: \n1 - Numeros pares de 0 a 100\n2 - bhaskara de 3 valores\
                      \n3 - 6 entradas para numeros positivos e media\n4 - Soma dos numeros impares no intervalo\n0 - Sair\n\n -->"))
    '''
    Tentei fazer uma verificação se a entrada do usuário é um valor valido
    if escolha != type(int):
        while(escolha != type(int)):
            escolha = input("Valor inválido, insira novamente: ")'''

            


    if(escolha==1):
        pares()
    elif(escolha==2):
        bhaskara()
    elif(escolha==3):
        positivosemedia()
    elif(escolha==4):
        somadenumerosimpares()
    elif(escolha==0):
        print("<---Fim--->")
    
escolha()