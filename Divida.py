divida = float(input("Valor da divida: "))
juros = float(input("Juros: "))
pagar = float(input("Valor a ser pago: "))
x = 1
while divida > pagar:
    divida = (divida + (divida * juros/100))
    print("%02d° mes sua divida está em %5.2f" %(x,divida))
    divida -= pagar
    print("===========")
    print("Valor após desconto mensal %5.2f" %divida)
    x += 1