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
        # Asegurarse de que la vida no baje de cero
        enemigo.vida = max(0, enemigo.vida - daño)
        print(self.nombre, "Ha realizado", daño, "puntos de daño a", enemigo.nombre)
        print("Vida de", enemigo.nombre, "es", enemigo.vida)

class Guerrero (Personaje):
    #Sobrescribir constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada 

    #Sobrescribir impresion
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-Espada:", self.espada)
        
    def elegir_arma(self):
        opcion = int(input("Elige un arma: \n(1)lanza de obsidiana, dmg 10 \n(2)Lanza de chaya, dmg 6\n<<"))
        if opcion == 1:
            self.espada = 10
        elif opcion == 2:
            self.espada == 5
        else:
            print("Opcion no valida")
            self.elegir_arma()
    
    #Sobrescribir calculo de dmg
    def dmg(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa
 
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

michael_jackson = Personaje("***Michael Jackon***", 20, 15, 10, 100)           
tlatoani = Guerrero("***Apocalipto***", 50, 70, 30, 100, 5)
merlin = Mago("**Merlin***", 20, 15, 10, 100, 5)

#tlatoani.elegir_arma()
#merlin.elegir_arma()

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
'''
# Ejemplo de uso
mi_personaje = Personaje('DRILLO', 40, 10, 30, 100)
mi_personaje.imprimir_atributos()
mi_enemigo = Personaje("Vergil", 70, 30, 70, 100)
mi_personaje.atacar(mi_enemigo)
'''