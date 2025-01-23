class Personaje:
    # Constructor de la clase
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def imprimir_atributos(self):
        print(self.nombre)
        print("-Fuerza:", self.fuerza)
        print("-Inteligencia:", self.inteligencia)
        print("-Defensa:", self.defensa)
        print("-Vida:", self.vida)
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza   
        self.inteligencia += inteligencia
        self.defensa += defensa
    
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "Ha muerto")
        return self.vida <= 0
    
    def dmg(self, enemigo):
        # Si la defensa del enemigo es mayor o igual que la fuerza del atacante, el daño es 0
        return max(0, self.fuerza - enemigo.defensa)
    
    def atacar(self, enemigo):
        daño = self.dmg(enemigo)
        enemigo.recibir_daño(daño)
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)

    def recibir_daño(self, daño):
        self.vida = max(0, self.vida - daño)

class Guerrero(Personaje):
    # Sobrescribir constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada, escudo):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
        self.escudo = escudo
        self.vida_escudo = defensa * escudo

    # Sobrescribir impresión
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-Espada:", self.espada)
        print("-Escudo:", self.escudo, "(Vida del escudo:", self.vida_escudo, ")")

    # Sobrescribir cálculo de daño
    def dmg(self, enemigo):
        return max(0, self.fuerza * self.espada - enemigo.defensa)

    # Sobrescribir recibir daño para manejar el escudo
    def recibir_daño(self, daño):
        if self.vida_escudo > 0:
            if daño < self.vida_escudo:
                self.vida_escudo -= daño
                print(self.nombre, "ha absorbido el daño con el escudo. Vida del escudo restante:", self.vida_escudo)
            elif daño == self.vida_escudo:
                self.vida_escudo = 0
                print(self.nombre, "ha perdido el escudo. Ahora está desprotegido.")
            else:
                daño_restante = daño - self.vida_escudo
                self.vida_escudo = 0
                print(self.nombre, "ha perdido el escudo. Daño restante aplicado a la vida:", daño_restante)
                super().recibir_daño(daño_restante)
        else:
            super().recibir_daño(daño)

# Método de combate por turnos
def combate(personaje1, personaje2):
    turno = 1
    while personaje1.esta_vivo() and personaje2.esta_vivo():
        print(f"\n--- Turno {turno} ---")
        personaje1.atacar(personaje2)
        if personaje2.esta_vivo():
            personaje2.atacar(personaje1)
        turno += 1

    if personaje1.esta_vivo():
        print(f"\n{personaje1.nombre} ha ganado el combate.")
    else:
        print(f"\n{personaje2.nombre} ha ganado el combate.")
 
class Mago (Personaje):
    #Sobrescribir constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro 

    #Sobrescribir impresion
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-Libro:", self.libro)
        
    def elegir_arma(self):
        opcion = int(input("Elige un arma: \n(1)Hechizoz de programacion, dmg 10 \n(2)Recetario de chaya, dmg 6\n<<"))
        if opcion == 1:
            self.libro = 10
        elif opcion == 2:
            self.libro == 5
        else:
            print("Opcion no valida")
            self.elegir_arma()
    
    #Sobrescribir calculo de dmg
    def dmg(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa

#michael_jackson = Personaje("***Michael Jackon***", 40, 15, 10, 100)           
#tlatoani = Guerrero("***Apocalipto***", 50, 70, 30, 100, 5, 2)
#merlin = Mago("**Merlin***", 20, 15, 10, 100, 5)

"""
tlatoani.elegir_arma()
merlin.elegir_arma()

#Imprimir atributos antes de la tragedia
tlatoani.imprimir_atributos()
merlin.imprimir_atributos()
michael_jackson.imprimir_atributos()

#Ataques masivos nucleares 3000
michael_jackson.atacar(tlatoani)
tlatoani.atacar(merlin)
merlin.atacar(michael_jackson)

#Imprimir atributos despues de la tragedia
tlatoani.imprimir_atributos()
merlin.imprimir_atributos()
michael_jackson.imprimir_atributos()
"""
# Ejemplo de uso
if __name__ == "__main__":
    tlatoani = Guerrero("***Apocalipto***", 1, 70, 5, 100, 5, 2)
    merlin = Mago("**Merlin***", 1, 1, 10, 100, 7)

    tlatoani.imprimir_atributos()
    merlin.imprimir_atributos()

    combate(tlatoani, merlin)

    tlatoani.imprimir_atributos()
    merlin.imprimir_atributos()

'''
# Ejemplo de uso
mi_personaje = Personaje('DRILLO', 40, 10, 30, 100)
mi_personaje.imprimir_atributos()
mi_enemigo = Personaje("Vergil", 70, 30, 70, 100)
mi_personaje.atacar(mi_enemigo)
'''