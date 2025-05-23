#Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

#Entrada
#Leia três valores de ponto flutuante (double) A, B e C.

#Saída 10.0 20.1 5.1
#Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.

a,b,c = map(float, input().split())
D =  (b**2 - 4*a*c)


if a == 0 or D < 0:
    print("Impossivel calcular")
else:
    R1 = (-b + D**0.5) / (2*a)
    R2 = (-b - D**0.5) / (2*a)
    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")