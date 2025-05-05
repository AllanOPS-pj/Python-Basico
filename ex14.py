
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

