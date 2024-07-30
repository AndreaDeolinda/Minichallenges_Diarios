# Escribir un programa que llene un arreglo unidimensional al azar utilizando una función
# y carge en un vector de 100 digitos e indique cuantos elementos son positivos y negativos
arreglo=[]
for i in range(100):
numero_entero = random.randint(1, 1000)
print(f"Número entero aleatorio:", numero_entero)
arreglo.append(numero_entero)