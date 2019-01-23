#CONVERTER DIAS EM SEGUNDOS
dias = int(input("Dias: "))
horas = int(input("Horas: "))
minutos = int(input("minutos :"))
segundos = int(input("Segundos :"))

segundos += minutos*60
segundos += horas*3600
segundos += dias*86400
print(segundos)