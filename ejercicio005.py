#ingrese un numero y diga si es par o impar 
"""dotstring
1. pedir al usuario ingresar un numero 
2. hacer el calculo para ver si es par o impar
3. mostrar el mensaje
"""
numero =int (input("ingrese el numero: "))
if (numero == 0): #si el numero es igual a cero
    print("cero")
elif (numero %2 == 0) :
    print (f"el numero es par ") #caso contrario si el numero mod 2 es cero
else: #caso contrario
    print (f"el numero es impar ") 