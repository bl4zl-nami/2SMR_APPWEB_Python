#Iván Jiménez Álvarez
#30/09/2024
#Este codigo te pide un numero par e impar, si los valores  no son corrector muestra un aviso
print("PAR E IMPAR (1)")
x = input("Escribe un numero par: ")
y = input("Escirbe un numero impar ")
x = eval(x)
y = eval(y)
if x%2 == 0 and y%2 == 1:
    print("gracias por colaborar!")
else: 
    print("Uno o mas de los valores no son correctos")
    print("Ejecute de nuevo el programa para volver a intentar ")