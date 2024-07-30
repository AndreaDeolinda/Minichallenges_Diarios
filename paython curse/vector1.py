# Realizar un programa que rellene un vector de Tamaño N con valores ingresados por el 
# usuario y muestre por pantalla el promedio de la suma de todos los valores ingresados
Tamaño_del_vector = int(input("Ingrese tamaño del vector: "))

# Inicializar una lista vacía para almacenar los elementos del vector
vector = []
for i in range(Tamaño_del_vector):
    elemento= int(input(f"Ingrese el valor del elemento {i+1}= "))
    vector.append(elemento)
suma=sum(vector)
promedio=suma//Tamaño_del_vector
print(f"la suma de dichos valores es= {suma}")
print(f"el promedio de dichos valores es= {promedio}")
