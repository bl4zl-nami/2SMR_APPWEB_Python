#Iván Jiménez Álvarez
#14/10/2024
#Este programa modifica el programa anterior de manera que las listas se escriban al final del programa.

NUML = int(input("Cuantas listas quiere crear?: "))

listas = []

for i in range(NUML):
    print("Cuantas palabras tiene la lista",str(i+1), "?: ")
    NUMP = int(input())

    NUML = []

    for j in range(NUMP):
        print("Digame la palabra ",str(j+1),": ")
        palabra = input()
        NUML.append(palabra)

    listas.append(NUML)

print()
for i in range(len(listas)):
    print("Lista ",str(i+1),": ",str(listas[i]))