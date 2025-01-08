class Personaje:
    #Atributos de la clase
    nombre = 'Default'
    fuerza = 0
    inteligencia = 0
    defensa = 0 
    vida = 0
    #Indica que no se haga nada en este momento.
    pass
mi_personaje = Personaje()
mi_personaje.nombre = "DRILLO"
mi_personaje.fuerza = 30
mi_personaje.inteligencia = 50
mi_personaje.defensa = 20
mi_personaje.vida = 10
print("El nombre del personaje es ", mi_personaje.nombre)
print("La fuerza del personaje es ", mi_personaje.fuerza)
print("La inteligencia del personaje es ", mi_personaje.inteligencia)
print("La defensa del personaje es ", mi_personaje.defensa)
print("La vida del personaje es ", mi_personaje.vida)