#Iván Jiménez Álvarez
#09/10/2024
#Este programa pide un numero entero mayor que cero y te escribe usu divisores

print("DIVISORES")
NUM = eval(input("escribe un nuemro entero mayor que cero! "))

if NUM < 0:
    print("te he pedido un numero entero mayor que cero")
else:
    print("los divisores de", NUM ,"son:", end = " ")
    for D in range(1,NUM+1):
        if NUM % D == 0:
            print(D,end=" ")