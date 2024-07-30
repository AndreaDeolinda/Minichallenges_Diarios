# Escribir un programa que almacene en un arreglo unidimensional 10 datos e indique cuantos
# elementos positivos hay en el mismo
contador=0
contadorimpar=0
vector = []
for i in range(10):
    elemento=int(input(f"ingrese el  valor para la posicion= {i+1} :"))
    vector.append(elemento)
    if elemento % 2 == 0 :
        contador +=1
    elif elemento % 2 == 1 :
        contadorimpar +=1 
print(f"la cantidad de elementos pares son= {contador}")
print(f"la cantidad de elementos impares son= {contadorimpar}")

    
