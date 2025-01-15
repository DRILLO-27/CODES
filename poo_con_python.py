class Personaje:
    # Constructor de la clase
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida

    def imprimir_atributos(self):
        print(self.__nombre)
        print("-Fuerza:", self.__fuerza)
        print("-Inteligencia:", self.__inteligencia)
        print("-Defensa:", self.__defensa)
        print("-Vida:", self.__vida)
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.__inteligencia += inteligencia
        self.__defensa += defensa
    
    def esta_vivo(self):
        return self.__vida > 0
    
    def __morir(self):
        self.__vida = 0
        print(self.__nombre, "Ha muerto")
        return self.__vida <= 0
    
    def dmg(self, enemigo):
        # Si la defensa del enemigo es mayor o igual que la fuerza del atacante, el daño es 0
        return max(0, self.__fuerza - enemigo.__defensa)
    
    def atacar(self, enemigo):
        daño = self.dmg(enemigo)
        # Asegurarse de que la vida no baje de cero
        enemigo.__vida = max(0, enemigo.__vida - daño)
        print(self.__nombre, "Ha realizado", daño, "puntos de daño a", enemigo.__nombre)
        print("Vida de", enemigo.__nombre, "es", enemigo.__vida)
    
    def get_fuerza(self):
        return self.__fuerza
    
    def set_fuerza(self, fuerza):
        if fuerza < 0:
            print("Error, valor negativo")
        else:
            self.__fuerza = fuerza

# Ejemplo de uso
mi_personaje = Personaje('DRILLO', 170, 10, 30, 100)
#mi_personaje.imprimir_atributos()
#mi_enemigo = Personaje("Vergil", 70, 30, 70, 100)
#mi_personaje.atacar(mi_enemigo)
#mi_personaje.fuerza
#mi_personaje.fuerza = 0
mi_personaje.set_fuerza(-5)
print(mi_personaje.get_fuerza())

