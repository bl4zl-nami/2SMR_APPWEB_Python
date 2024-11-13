#Iván Jiménez Álvarez
#04/10/2024
#Este programa pide 2 numeros enteros y pone si el mayoe es multiplo del menos, cuando sea negativo tiene que avisar
print("COMPARADOR DE MÚLTIPLOS")
MUL1 = eval(input("Escribe un número "))
MUL2 = eval(input("Escribe otro numero "))

if MUL1 < 0 or MUL2 < 0:
    print("No se puede con mueros negativos")

elif MUL1 == 0 or MUL2 == 0:
    print("No valen valores nulos")

elif MUL1 >= MUL2:
    if MUL1%MUL2 == 0:
        print(MUL1,"es multiplo de",MUL2)
    else: 
        print(MUL1,"no es multiplo de",MUL2)

elif MUL2 >= MUL1:
    if MUL2%MUL1 == 0:
        print(MUL2,"es multiplo de",MUL1)
    else: 
        print(MUL2,"no es multiplo de",MUL1)