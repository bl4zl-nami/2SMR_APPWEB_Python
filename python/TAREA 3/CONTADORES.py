#Iván Jiménez Álvarez
#09/10/2024
#Este programa te pide cuantos numeros vas a introducir y luego te dice cuantos son negativos

print("NÚMEROS NEGATIVOS")
NUMLIST = eval(input("¿Cuantos valores vas a introducir? "))
cont = 0

if NUMLIST < 0:
    print("imposible!!!")
else:
    for L in range(1,NUMLIST+1):
        NUM = eval(input("Escriba el numero: "))
        if NUM < 0:
            cont = cont + 1
print("ha escrito", cont,"numeros negativos")