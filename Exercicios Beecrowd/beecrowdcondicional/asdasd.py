
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

selecao1()