# 3- Escribir un programa que almacene una contraseña en una variable,
# y pregunte al usuario por la contraseña hasta que introduzca la contraseña
# correcta.

# Cuando el usuario ingrese la contrasena correcta,
# imprimir un mensaje secreto
contrasenha_a_adivinar = "ANdReADeO"
while True:
    ingresar_contra = input("Ingrese la contrasenha= ")
    if ingresar_contra == contrasenha_a_adivinar:
        print ("Bienvenido a tu banco")
        break
    else:
        print("La contrasenha es incorrecta vuelva a ingresar")