# ingresa 5 edades, almacenarlos en un arreglo y mostrarlos
arreglo=[]
for i in range(5):
    edades=int(input(f"ingrese el valor de 5 edades en la posición {i+1}= "))
    arreglo.append(edades)
print("*MOSTRAR EDADES*")
for i in range(len(arreglo)):
    print(f"mostrar edad= {arreglo[i]} en la posición: {i + 1}")