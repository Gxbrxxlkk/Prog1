"""9. Escreva um script que solicite ao usuário um número inteiro de cinco dígitos. Em seguida, separe o 
número em seus dígitos individuais e os imprima, separados entre si por três espaços. Por exemplo, se o usuário digitar 
o número 42339, o script deverá imprimir 4 2 3 3 9. Suponha que o usuário 
entre com o número correto de dígitos. Dica: Use as operações de divisão inteira e módulo para separar os dígitos."""

numero = int(input("insira um numero inteiro de 5 digitos:"))
primeiro = numero // 10000
segundo = ((numero // 1000)-10)
terceiro = ((numero // 100)-100)%10
quarto = (((numero // 10)-1000)%100)%10
quinto = (((((numero // 1)-10000)%1000)%100)%10)
print(primeiro," ",segundo," ",terceiro," ",quarto," ",quinto)
