#Iván Jiménez Álvarez
#14/10/2024
#Este programa pide dos números enteros y escriba la lista de números consecutivos que hay entre ellos, de menor a mayor.

altura = int(input("Introduce la altura del triángulo: "))

for i in range(altura):
    print("* " * (i + 1))
for i in range(altura - 1, 0, -1):
    print("* " * i)