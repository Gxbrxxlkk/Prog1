"""Alguns consultores de investimentos dizem que é razoável esperar um retorno de 7% ao ano no longo prazo no mercado de ações. Solicite ao usuário 
o valor investido e calcule quanto dinheiro ele terá após 10, 20 e 30 anos. Use a seguinte fórmula para determinar esses valores: a=p(1+r)n onde p 
é o valor original investido, r é a taxa de retorno anual (7%), n é o número de anos (10, 20 ou 30) e a é o valor obtido no final do enésimo ano."""

entrada = float(input("Insira o valor que gostaria de investir:"))

valor_10 = entrada*(1+0.07)**10
valor_20 = entrada*(1+0.07)**20
valor_30 = entrada*(1+0.07)**30
print("Valor daqui a 10 anos:",valor_10)
print("Valor daqui 20 anos:",valor_20)
print("Valor daqui a 30 anos:",valor_30)