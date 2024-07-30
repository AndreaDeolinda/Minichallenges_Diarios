#Escribir un programa que el usuario ingrese el tamaño del vector
#  y el programa llene con ceros en los posiciones pares y uno en las
# Y uno en las posiciones impares.
tamaño_vector= int(input("ingrese tamaño del vector= "))
vector=[]
for i in range(tamaño_vector):
    if i % 2 == 0 :
        valor=0
    else :
        valor=1
    input(f"el valor para la posición= {i} es= {valor}")