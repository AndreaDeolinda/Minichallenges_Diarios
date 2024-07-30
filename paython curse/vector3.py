# Crear un vector que contenga notas de 50 supuestos estudiantes con valores entre 0 y 20
# Luego de acuerdo a las notas contenidas el programa debe indicar cuantos estudiantes son
#Deficientes de o a 5 puntos 
#Regulares de 6 a 7 puntos 
#Buenos de 11 a 15 puntos
#Excelentes de 16 a 20 puntos
tamaño_vector= int(input("ingrese el numero de estudiantes "))
vector=[]
contador=0
contRe=0
contBue=0
contExc=0
for i in range(tamaño_vector):
    Nota=int(input(f"ingrese la nota del estudiante {i+1} = "))
    vector.append(Nota)
    if Nota >= 0 and Nota <= 5 :
        print("El alumno es Deficiente")
        contador += 1
    elif Nota >=6 and Nota <= 10 :
        print("El alumno es Regular")
        contRe += 1
    elif Nota >=11 and Nota <= 15 :   
        print("El alumno es Bueno")
        contBue += 1
    elif Nota >=16 and Nota <= 20 :
        print("El alumno es Excelente")
        contExc += 1
    else:
        print("La nota ingresada esta fuera de los parametros")   

print(f"La cantidad de alumnos deficientes son= {contador}")
print(f"La cantidad de alumnos Regulares son= {contRe}")
print(f"La cantidad de alumnos Buenos son= {contBue}")
print(f"La cantidad de alumnos Excelentes son= {contExc}")
    
    
    
    
    