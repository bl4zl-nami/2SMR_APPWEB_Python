#Ivan Jimenez Alvarez 2ºSMRA
#02/10/2024
#Este programa nos pasa los segundos a horas y minutos
print("CONVERTIDOR DE SEGUNDOS A HORAS Y MINUTOS")
SEG = eval(input("Escribe una cantidad de segundos: "))
horas = SEG // 3600
minutos = (SEG % 3600) // 60
segundos = SEG % 60
print(SEG, "segundos son", horas, "horas,", minutos, "minutos y", segundos, "segundos")