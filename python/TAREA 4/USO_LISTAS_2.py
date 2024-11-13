#Iván Jiménez Álvarez
#09/10/2024
#Este programa te pide 2 numeros enteros y te pide escribir una lista con los numero s de menos a mayor que hay entre ellos

print("LISTA DE MENOS A MAYOR")
NUM1 = eval(input("Escriba un numero entero: "))
NUM2 = eval(input("Escribe otro numero entero: "))

if NUM1 < NUM2:
    print(list(range(NUM1,NUM2)))
else:
    print(list(range(NUM2,NUM1)))