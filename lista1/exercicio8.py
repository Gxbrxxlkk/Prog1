""". Escreva um script que solicite três números inteiros ao usuário. Então, exiba a soma, a média, o produto, o menor e o maior dos números."""



numero1 = int(input("Insira seu primeiro valor:"))

numero2 = int(input("Insira seu segundo valor:"))

numero3 = int(input("Insira seu terceiro valor:"))

media = (numero1 + numero2 + numero3)/3

soma = numero3 + numero2 + numero1
produto = numero2 * numero3 * numero1
print("Sua soma é:", soma)
print("Sua média é:", media)
print("Seu produto é:", produto)
if(numero1 < numero2 and numero1 < numero3):
    print("Seu primeiro valor é o menor")

elif(numero2 < numero3):
    print("Seu segundo valor é menor")

else:
    print("Seu terceiro valor é menor")

if(numero1 > numero2 and numero1 > numero3):
    print("Seu primeiro valor é o maior")

elif(numero2 > numero3):
    print("Seu segundo valor é maior")

else:
    print("Seu terceiro valor é maior")