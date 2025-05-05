#Escreva um programa em Python 3 para calcular o valor final de um pedido de pizza. Seguem os valores para os três tamanhos disponíveis:

#P: R$ 15.00
#M: R$ 18.50
#G: R$ 23.00
#O cliente pode pedir adicional de queijo, que custa R$ 2.50 para uma pizza pequena e R$ 4.00 para uma pizza média ou grande. Além disso, o cliente pode optar pela borda recheada, que custa R$ 5.00, independente do tamanho.

#O seu programa deve ler o tamanho da pizza (P, M ou G), a opção pelo adicional de queijo (S ou N) e a opção pela borda recheada (S ou N). Seu programa deve imprimir o valor total do pedido, seguindo a formatação dos exemplos.

#Por exemplo:

#Entrada	Resultado
#P N N
#Total: R$ 15.00
#M S N
#Total: R$ 22.50


valor_total = 0

tamanho = str(input())
adicional_queijo = str(input())
borda_recheada = str(input())

if tamanho == "P":
    valor_total = 15
elif tamanho == "M":
    valor_total = 18.5
elif tamanho == "G":
    valor_total = 23
else:
    valor_total = 0

    
if adicional_queijo == "S" and tamanho == "P":
    valor_total = valor_total + 2.5
elif adicional_queijo == "S" and (tamanho == "M" or tamanho == "G"):
    valor_total = valor_total + 4

if borda_recheada == "S":
    valor_total = valor_total + 5

print(f"Total: R${valor_total:.2f}")



    





