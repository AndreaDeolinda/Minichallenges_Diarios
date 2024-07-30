 
nombre = input ("Ingrese su nombre")
edad = int (input ("Ingrese su edad")) #El input equivale a leer#
print (f"Hola {nombre} . Tu edad es: {edad}")

input("Bienvenido a la discoteca")
input("solo se permite el paso a mayores de edad y menores de  65 años")
edad = int (input("ingrese su edad para ingresar a la discoteca"))
if edad <=17 : #si
    input("Eres menor de edad")
elif edad >= 65: #sino
    input("No puedes ingresar estás mayor")  
else:         #si no si
    input("puedes ingresar a la fiesta")
