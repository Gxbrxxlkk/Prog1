def vetor():

    nuimeros = [1 ,2 ,3 ,4, 5,6 , 7, 8, 9, 0]
    print(len(nuimeros))
    for i in range(len(nuimeros)): #range vai sempre um numero a menos do valor, como ali o len vale 10, ele vai iterar 9 vezes, o valor do vetor(Adicione +1 para ver o erro)
        (f'{i} : {nuimeros[i]}')

def vetor2(lista1, lista2):

    if(len(lista1) == len(lista2)):
        for i in range(len(lista2)):
            if (lista1[i] != lista2[i]):
                return False
            else: True
    else: 
        False

#lista1 = [1, 2, 3, 4, 5, 6]
#lista2 = [1, 2 ,3, 4, 5, 6]

#res = vetor2(lista1, lista2)
#print(res)

def listacubo(numeros):

    for i in range(len(numeros)):
        numeros[i] = numeros[i]**3
    return print(numeros)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#caracteres = []
#caracteres += 'Aniversário'
#print(caracteres)

#aaa = ("red",)
#id(aaa)

#tupla1 = (4, 5 , 6)
#lista1 = [1, 2 , 3]
#res = lista1 + tupla1
#print(res)
numero1, numero2, numero3 = range(10, 40, 10) #
print(f'{numero1} , {numero2}, {numero3}') 

nomes = ["Clara", "Fernanda", "Jéssica"]
list(enumerate(nomes))

for i, nome in enumerate(nomes):
    print(f'{i} : {nome}')