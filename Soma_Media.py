soma = 0
media = 0
x = 0
while True:
    numero = int(input("Digite um numero (ZERO para sair): "))
    if numero == 0:
        print("Você digitou %d Numeros, totalizando %d e a média %5.2f" %(x,soma,media))
        break
    soma += numero
    x += 1
    media = soma / x
