print("holiii")

deportes=["Futbol","Voleibol","Natacion","Basquetbol"]

print(deportes[2])

#Posicion de natacion
pos=deportes.index("Natacion")
print("La posicion de natacion es: ", pos)
print(deportes.index("Natacion"))

#Agregar otro deporte al final
deportes.append("handball")
print(deportes)

#Afgregar otro deporte en una posicion especifica
deportes.insert(2,"tennis")
print(deportes)