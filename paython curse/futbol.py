# El seleccionado de Paraguay disputa sus tres partidos de la primera fase de un torneo
# donde se registran los datos NRO DE partido equipo, equipo contrincante, goles a favor 
# goles en contra.
# Realiza un codigo que calcule e imprima 
# a) El puntaje obtenido al final de la primera fase (3 puntos si gana, 1 punto empate
#                                                     ,0 si pierde)
# b) La cantidad de goles que obtuvo y cuantos le hicieron 
# c)El promedio de goles en los tres partidos.
#un equipo tres partidos diferentes con tres con TRES CONTRINCANTES DIFERENTES

print("***********************LA SELECCION PARAGUAYA- TORNEO**************************")

suma=0
c_f=0
c_c=0

for i in range(3):
    numero_de_patido=int(input("ingrese numero de partido= "))
    contrincante=(input("ingrese nombre del equipo contrincante= "))
    golesafavor=int(input("ingrese numero de goles a favor= "))
    golescontra=int(input("ingrese numero de goles en contra= "))

    c_f +=golesafavor
    c_c +=golescontra

    if golesafavor>golescontra :
        print("gano el partido") 
        suma += 3 
    elif golesafavor == golescontra :
        print("Empato el partido")
        suma += 1
    else :
        print("Perdió el partido")
        suma += 0
    
Promedio_de_goles=c_f//3
print(f"El puntaje obtenido al final de la fase es= {suma}")
print(f"La cantidad de goles que obtuvo= {c_f}")
print(f"La cantidad de goles en contra= {c_c}")
print(f"El promedio de Goles en los tres partidos= {Promedio_de_goles}")





   




  