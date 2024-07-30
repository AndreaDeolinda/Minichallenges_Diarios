#Solicitar 10 números, Cargarlos en un vector e imprimirlos por pantalla, Según 
#su posición cargada
lista=[]
for i in range(10):
    digito=int(input(f"ingrese el valor para la posición {i+1}= "))
    lista.append(digito)

for i in range(len(lista)):
    print(f"el valor cargado en la posición: {i+1} es = {lista[i]}")
