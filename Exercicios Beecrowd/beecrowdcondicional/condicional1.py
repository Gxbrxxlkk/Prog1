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

    valor1, valor2, valor3 = map(float, input().split())
    print(f"{type(valor1)} {type(valor2)} {type(valor3)}")



    delta = (valor2**2 -4*valor1*valor3)
    raizdelta= delta**(1/2)
    raiz1 = 0
    raiz2 = 0


    if(delta < 0):
        print("Imposivel calcular")

    elif(valor1 == 0):
        print("Imposivel calcular")
            
    elif(raizdelta == 0):
        
        raiz1 = ((-1*valor2) + raizdelta)/(2*valor1)
        raiz2 = ((-1*valor2) - raizdelta)/(2*valor1)

        print(f"R1 = {raiz1:.5f}\nR2 = {raiz2:.5f}")
    
    elif(raizdelta > 0):

        raiz1 = ((-1*valor2) + raizdelta)/(2*valor1)
        raiz2 = ((-1*valor2) - raizdelta)/(2*valor1)

        print(f"R1 = {raiz1:.5f}\nR2 = {raiz2:.5f}")
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

def soma():
    A = int(input())
    B = int(input())
    X = A + B
    print("X =", X)
    escolha()

def intervalo(): #colocar nas escolhas na def escolha

    valor = float(input())

    if(valor >=0 and valor <= 25):
        print("Intervalo [0,25]")
    elif(valor >25 and valor<=50):
        print("Intervalo (25,50]")
    elif(valor > 50 and valor<=75):
        print("Intervalo (50,75]")
    elif(valor >75 and valor<=100):
        print("Intervalo (75,100]")
    else: 
        print("Fora de intervalo")

def lanche():
    """Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e \
    mostre o valor da conta a pagar.
    Entrada
    O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.
    Saída
    O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal."""
    pedido, qtd = map(int, input().split()) # nao esquecer de colocar aspas na frente do split, ele é uma funçao e nao consegue ser iterado sem, codigo vai por agua a baixo
    if(pedido == 1):
        pedido = 4.00
    elif(pedido == 2):
        pedido = 4.50
    elif(pedido == 3):
        pedido = 5.00
    elif(pedido == 4):
        pedido = 2.00
    elif(pedido == 5):
        pedido = 1.50
    
    vlfnl = pedido*qtd
    print(f"Total: R$ {vlfnl:.2f    }")


def dstpontos():
    
    
    a, b = map(float, input().split())
    c, d = map(float, input().split())
    dx = c - a
    dy = d - b
    dp = ((dx**2) + (dy**2))**(1/2)

    print(f"{dp:.4f}")

def dinheiro():
    """Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. 
    As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.
    Entrada
    O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).
    Saída
    Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. 
    Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”."""

    A = int(input())
    nota100 = A//100
    nota50 = (A%100)//50
    nota20 = ((A%100)%50)//20
    nota10 = (((A%100)%50)%20)//10
    nota5 = ((((A%100)%50)%20)%10)//5
    nota2 = (((((A%100)%50)%20)%10)%5)//2
    nota1 = ((((((A%100)%50)%20)%10)%5)%2)//1
    
    print(f"{A}\n{nota100} nota(s) de R$ 100,00\n{nota50} nota(s) de R$ 50,00\n{nota20} nota(s) de R$ 20,00\n{nota10} nota(s) de R$ 10,00\n\
{nota5} nota(s) de R$ 5,00\n{nota2} nota(s) de R$ 2,00\n{nota1} nota(s) de R$ 1,00")


def dinheirogpt():
    A = int(input())
    print(A)

    notas = [100, 50, 20, 10, 5, 2, 1]

    for nota in notas:
        quantidade = A // nota
        print(f"{quantidade} nota(s) de R$ {nota},00")
        A %= nota


def idade(): #lembrar de quando usar módulo, criar uma variavel armazenando o que restou, facilita as contas e n precisa fazer o q fez acima
    dias = int(input())
    anos = dias//365
    dias_restantes = dias%365
    meses = dias_restantes//30
    dias_restantes = dias_restantes %30

    print(f"{anos} ano(s)\n{meses} mes(es)\n{dias_restantes} dia(s)")


def dinheiromoeda():

    A = float(input())
    nota100 = A//100
    nota50 = (A%100)//50
    nota20 = ((A%100)%50)//20
    nota10 = (((A%100)%50)%20)//10
    nota5 = ((((A%100)%50)%20)%10)//5
    nota2 = (((((A%100)%50)%20)%10)%5)//2
    moeda1 = ((((((A%100)%50)%20)%10)%5)%2)//1
    A = ((A-(int(A)))*100)
    moeda50= A//50
    moeda25= (A-(moeda50*50))//25
    moeda10= (A-(moeda50*50)-(moeda25*25))//10
    moeda5= (A-(moeda50*50)-(moeda25*25)-(moeda10*10))//5
    moeda01= (A-(moeda50*50)-(moeda25*25)-(moeda10*10)-(moeda5*5))//1

    print(f"NOTAS:\n{int(nota100)} nota(s) de R$ 100.00\n{int(nota50)} nota(s) de R$ 50.00\n{int(nota20)} nota(s) de R$ 20.00\n{int(nota10)} nota(s) de R$ 10.00\n\
{int(nota5)} nota(s) de R$ 5.00\n{int(nota2)} nota(s) de R$ 2.00\nMOEDAS:\n{int(moeda1)} moeda(s) de R$ 1.00\n{int(moeda50)} moeda(s) de R$ 0.50\n{int(moeda25)} moeda(s) de R$ 0.25\n\
{int(moeda10)} moeda(s) de R$ 0.10\n{int(moeda5)} moeda(s) de R$ 0.05\n{int(moeda01)} moeda(s) de R$ 0.01")
    
def dinheiromoedagpt():
    # Leitura do valor monetário
    valor = float(input())

    # Cálculo das notas
    notas = [100, 50, 20, 10, 5, 2]
    moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

    # Parte inteira para notas
    parte_inteira = int(valor)

    # Parte decimal para moedas
    parte_decimal = round((valor - parte_inteira) * 100)

    print("NOTAS:")

    # Processamento das notas
    for nota in notas:
        quantidade_notas = parte_inteira // nota
        print(f"{quantidade_notas} nota(s) de R$ {nota:.2f}")
        parte_inteira %= nota

    print("MOEDAS:")

    # Processamento das moedas
    # Primeiro, lidamos com a moeda de 1 real (que é a parte inteira restante)
    quantidade_moeda1_real = parte_inteira // 1
    print(f"{quantidade_moeda1_real} moeda(s) de R$ 1.00")
    parte_decimal += parte_inteira * 100

    # Agora, as moedas fracionadas
    for moeda in moedas[1:]:
        quantidade_moedas = parte_decimal // int(moeda * 100)
        print(f"{quantidade_moedas} moeda(s) de R$ {moeda:.2f}")
        parte_decimal %= int(moeda * 100)

def selecao1():
    A, B, C, D = map(int,input().split())#esse tipo de input é muito bom de usar, lembrar de como fazer para usar em formulas futuras

    if B > C and D > A and (C + D) > (A +B) and (C,D>0) and (A%2 == 0):
        print("Valores aceitos")

    else: print("Valores nao aceitos")




def escolha():
    while True:
        print("\n" + "-"*40)
        print("Escolha uma função:")
        print("1 - Números pares de 0 a 100")
        print("2 - Bhaskara de 3 valores")
        print("3 - Média de 6 números positivos")
        print("4 - Soma dos números ímpares no intervalo")
        print("5 - Soma")
        print("6 - Lanche")
        print("7 - Intervalo")
        print("8 - Lanche (opção duplicada)")
        print("9 - Distância de pontos")
        print("10 - Dinheiro")
        print("11 - Dinheiro GPT")
        print("12 - Idade")
        print("13 - Dinheiro Moeda")
        print("14 - Dinheiro Moeda GPT")
        print("15 - Seleção 1")
        print("0 - Sair")
        print("-"*40)
        
        try:
            escolha = int(input("Digite o número da função que deseja usar: "))
        except ValueError:
            print("Valor inválido, insira um número.")
            continue

        if escolha == 1:
            pares()
        elif escolha == 2:
            bhaskara()
        elif escolha == 3:
            positivosemedia()
        elif escolha == 4:
            somadenumerosimpares()
        elif escolha == 5:
            soma()
        elif escolha == 6:
            lanche()
        elif escolha == 7:
            intervalo()
        elif escolha == 8:
            lanche()
        elif escolha == 9:
            dstpontos()
        elif escolha == 10:
            dinheiro()
        elif escolha == 11:
            dinheirogpt()
        elif escolha == 12:
            idade()
        elif escolha == 13:
            dinheiromoeda()
        elif escolha == 14:
            dinheiromoedagpt()
        elif escolha == 15:
            selecao1()
        elif escolha == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

escolha()



#esse era o meu menu de escolha, fiquei com preguiça de formatar e usei o gpt pra fazer um

"""def escolha():
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
    elif(escolha==5):
        soma()
    elif(escolha == 6):
        lanche()
    elif(escolha == 7):
        intervalo()
    elif(escolha == 8):
        lanche()
    elif(escolha == 9):
        dstpontos()
    elif(escolha == 10):
        dinheiro()
    elif(escolha == 11):
        dinheirogpt()
    elif(escolha == 12):
        idade()
    elif(escolha == 13):
        dinheiromoeda()
    elif(escolha == 14):
        dinheiromoedagpt()
    elif(escolha == 15):
        selecao1()
    elif(escolha==0):
        print("<---Fim--->")
    
escolha()"""












