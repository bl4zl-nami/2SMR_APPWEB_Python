#Iván Jiménez Álvarez
#30/09/2024
#Este codigo te pide un mumero par y se el valor no es correcto muestra un aviso 
print("PAR E IMPAR (2)")
PAR = input("Escribe un nuemro par ")
PAR = eval(PAR)
if PAR%2 == 0:
    IMP = input("Escribe un numero impar ")
    IMP = eval(IMP)
    if IMP%2 == 1:
        print("Gracias por tu colaboración!")
    else:
        print("No se ha escrito un nummero impar")
        print("Ejecute de nuevo el programa para volver a intertarlo")
else:
    print("No se ha escrito un numero par")
    print("Ejecute de nuevo el programa para volver a intertarlo")