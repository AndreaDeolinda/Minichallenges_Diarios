# Una función en python es un conjunto 
# # de instrucciones que realizan una tarea en especifico.
# Las funciones son una forma de organizar y reutilizar el código para realizar tareas
# especificas. Al definir una funcion , le das un nombre a un bloque de codigo y puedes "llamar"
# a ese bloque de codigo por nombre en cualquier lugar de tu programa.

# Crea un codigo que ingrese dos numeros y al oprimir el numero uno ejecute una 
# fución
numero1 = int(input("ingrese un numero: "))
numero2 = int(input("ingrese otro numero: "))
def suma(numero1,numero2):
    operacion = numero1 + numero2
    print(f"{operacion}")
while  True :
    Valor= int(input("ingrese el valor que desee ejecutar la función al oprimir el nro 1: "))
    if Valor ==  1 :
        suma(numero1,numero2)
    else :
        input("no desea ejecutar la función")
    break

    