# Escribir un programa que busque un numero en un vector de 10 digitos ingresados por el 
#usuario e indique las posiciones e indique su ubicación
vector=[]
posicion=0
for i in range(10):
    valor=int(input(f"Ingresar el valor para la posición {i+1}= "))
    vector.append(valor)

buscar=int(input("ingrese el valor que desea buscar en el vector de 10 elementos= "))
posicion=[]
for i in range(len(vector)):
    if vector[i]==buscar : #aquí guarda a todos los valores que coinciden dentro de un vector
        posicion.append(i+1)
        
if posicion :
    print("El valor se encuentra en las siguientes posiciones")
    for pos in posicion:
        print(f"posición={pos}")
else:
    print("El valor no se encuentra en el vector")
   
