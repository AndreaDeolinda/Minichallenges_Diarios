# 2- Escribir un programa en el que se pregunte 
# al usuario por una temperatura (en grados Celsius), 
# imprima la temperatura escrita, y luego clasificar
# la temperatura ingresada en los siguientes niveles:
# Entre -10 y 18 grados, que imprima "Fresquete". 
# Entre 19 y 30 grados, que imprima "Calor'i". Entre
# 31 y 45 grados, que imprima "Hakuuuuuu". Para todo lo demás, 
# imprimir "Ñamano mba'e!"
Temperatura= int(input("Ingrese la Temperatura de hoy: "))
print (f"La temperatura del dia de hoy es: {Temperatura}")
if Temperatura >= -10 and Temperatura <= 18 :
    Print("fresquete")
elif Temperatura >= 19 and Temperatura <= 30 :
    print("Calor'i")
elif Temperatura >= 31 and Temperatura <= 45 :
    print("Hakuuuuu")
else:
    Print("Ñamano mba'e!")
