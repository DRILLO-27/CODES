from kivy.uix.recyclegridlayout import defaultdict
class Personaje:
    #Constructor de la clase
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre =  nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        #Que es self? Referencia al mismo objeto,
        #Que es init? constructor que inicializa el atributo del objeto
        #Por que empieza con doble guion bajo? Porque es un metodo magico
        #En que momento se utiliza el metodo init? Cuando se crea un objeto
    def imprimir_atributos(self):
        print(self.nombre)
        print("-Fuerza:", self.fuerza)
        print("-Inteligencia:", self.inteligencia)
        print("-Defensa:", self.defensa)
        print("-Vida:", self.vida)
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
    
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "Ha muerto")
        return self.vida <= 0
    
    def dmg(self, enemigo):
        return self.fuerza  - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.dmg(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "Ha realizado", daño, "puntos de daño a", enemigo.nombre)
        print("vida de", enemigo.nombre, "Es", enemigo.vida)
mi_personaje = Personaje('DRILLO',100, 10, 30, 100)
mi_personaje.imprimir_atributos()
mi_enemigo = Personaje("Vergil", 70, 30, 70, 100)
mi_personaje.atacar(mi_enemigo)
#print(mi_personaje.dmg(mi_enemigo))
# print(mi_personaje.esta_vivo())
# print(mi_personaje.morir())
# print("---------------------------------------")
# mi_personaje.subir_nivel(10, 1, 5)
# mi_personaje.imprimir_atributos()
