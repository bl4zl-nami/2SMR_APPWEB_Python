#Iván Jiménez Álvarez
#04/10/2024
#Este programa te pide tres numeros, si los 3 son iguales te lo dice,ny si hay solo 2 tambien o si son los 3 distintos
print("COMPARADOR DE TRES NUMEROS")
numero1 = eval(input("Escribe un número: "))
numero2 = eval(input("Escribe otro número: "))
numero3 = eval(input("Escribe otro número: "))
if numero1 and numero2 == numero3:
    print("Has puesto el mismo número las 3 veces")
elif numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
    print("Has puesto el mismo número 2 veces")
else:
    print("Los 3 numeros son distintos")