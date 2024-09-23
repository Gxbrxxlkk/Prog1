
'''
UFMT - Curso de Bacharelado em Ciência da Computação
Disciplina: Programação I
Professor: Ivairton M. Santos
Trabalho de análise e exploração de dados
'''
#####################
# importacao das bibliotecas usadas no projeto 
from sklearn.datasets import fetch_california_housing 
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
#####################
def Main(): # funcao main : criacao de um layout para o usuario escolher uma funcao 
    print('bem vindo ao programa prog')
    print('graficos[0] metricas[1] printagem DataFrame[2] correlação de valores[3]')
    while True:
        print("Por favor, digite um número de 0 a 3 ")
        entrada = input()
        try:
            numero = int(entrada)  # Tenta converter a entrada para um inteiro
            if 0 <= numero <= 3:  # Verifica se o número está entre 0 e 2
                return numero  # Retorna o número se estiver no intervalo
            else:
                print("O número não está nas opções acima, tente novamente")  # Mensagem de erro
        except ValueError:
            print("Entrada inválida. Tente novamente.")  # Mensagem de erro
#####################
# requisito 1
# manipulacao de dados e divisao de colunas  
ch = fetch_california_housing()
chd = ch.data
# criacao do dataframe e adicao da nova coluna [medhousevalue] 
cdf = pd.DataFrame(chd, columns=ch.feature_names)

# gerando nova coluna usando a funcao target
cdf['MedhouseValue'] = ch.target

# cdf.to_excel('oi.xlsx', index=False)  <----- ignora so para  test╰（‵□′）╯
#####################
# requisito 2
# criacao do grafico de pontos utilinzando o dataframe acima.
def ScatPlot():
    sns.scatterplot(data=cdf, x='Longitude', y='Latitude',hue='MedhouseValue',palette='viridis',legend=False)
#####################
vars = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup'] # variaveis utilizadas no requisito 3 e 4
# requisito 3

def CalMetricas(name : str):
    '''
    Funcao de calculos de metricas

    recebe : STR
    retorna : printagem das metricas
    '''

    # calculo das metricas
    media = cdf[name].mean() 
    mediana = cdf[name].median() 
    moda = cdf[name].mode()
    variancia = cdf[name].var() 
    desvio = cdf[name].std() 
    Q1 = cdf[name].quantile(0.25)
    Q2 = cdf[name].quantile(0.5)
    Q3 = cdf[name].quantile(0.75)
    IQR = Q3 - Q1

    # printagem das metricas
    print() # pula linha
    print(f"Média da variável {name}, {media}")
    print(f"Mediana da variável {name}, {mediana}")
    if name == 'MedInc':
        print(f"Moda da variável {name} {moda[0]} e {moda[1]}")
    else:
        print(f"Moda da variável {name} {moda[0]}")
    print(f"Variância da variável {name}, {variancia}")
    print(f"Desvio padrão da variável {name}, {desvio}")
    print('1o quartil =', Q1)
    print('2o quartil =', Q2, '(Mediana)')
    print('3o quartil =', Q3)
    print('Intervalo interquartil =', IQR)
    print() # pula linha
#####################
# requisito 4

# funcao para criar grafico boxplot
def BoxGraf(vars : list):
    '''
    funcao grafico histograma 

    recebe : uma lista de variaveis 
    retorna : plotagem do grafico
    '''
    fig, ax = plt.subplots(2, 3,figsize=(12, 7)) # funcao para criar graficos vazios em forma de matriz
    # loop para percorrer os graficos em forma de matriz e criar cada um separadamente
    for i in range(0,2):
        for j in range(0,3):
            # condicional para pular linha e evitar conflito entre graficos ja existentes 
            if i == 0:
                sns.boxplot(cdf[vars[j]], orient='h', ax=ax[i,j])
            else:
                sns.boxplot(cdf[vars[j+3]], orient='h', ax=ax[i,j])
    fig.tight_layout() # otimizar layout do grafico

# funcao para criar grafico histograma
def HistGraf(vars : list):
    '''
    funcao grafico histograma 

    recebe : uma lista de variaveis 
    retorna : plotagem do grafico
    '''
    fig, ax = plt.subplots(2, 3,figsize=(12, 7)) # funcao para criar graficos vazios em forma de matriz
    # loop para percorrer os graficos em forma de matriz e criar cada um separadamente
    for i in range(0,2):
        for j in range(0,3):
            # condicional para pular linha e evitar conflito entre graficos ja existentes 
            if i == 0:
                sns.histplot(cdf[vars[j]], ax=ax[i,j])
            else:
                sns.histplot(cdf[vars[j+3]], ax=ax[i,j])
    fig.tight_layout() # otimizar layout do grafico 
#####################

if __name__ == '__main__':
    entrada = Main() # entrada do usuario

    if entrada == 0: # resposta requisitos 2 e 4 : printagem dos graficos
        print('Aguarde...')
        ScatPlot() # grafico de pontos
        BoxGraf(vars) # grafico BoxPlot
        HistGraf(vars) # grafico Histograma
        print("nao esqueca de fechar todos os graficos para executar novamento o prog (●'◡'●)")
        plt.show() # printagem

    elif entrada == 1: # resposta requisito 3 : printagem das metricas
        for i in vars: # laco para printar todas as variaveis 
            CalMetricas(i) 

    elif entrada == 2 :                                                                     # <-- tirei o else e coloquei opção 2 para colocar mais opções, do requisito 5 e 6
        print(cdf.describe()) # resposta requisito 1 : printagem DataFrame.describe
    
    elif entrada == 3:  # Resposta do requisito 5 : correlação de conjunto de variaveis
        # Calculando a matriz de correlação
        correlacao = cdf.drop(columns=['Longitude', 'Latitude']).corr()

        print(correlacao)

        

"""
23/09/2024
Rascunho do Gabriel


# Requisito 5

correlacao = cdf.corr()
print(correlacao)

Vou ter q usar a função abs, de deixar o valor sempre positivo, pois existem correlações negativas que vão aumentar o valor do imovel, ex: menor idade do imovel e maior renda da familia que reside nele, maior o valor da casa

"""


