class Vehiculo():
    def __init__(self):
        self.largo = 50
        self.ancho = 25
        self.arrancando = False
    
    def arrancar(self,estado):
        print("Verificando...")
        self.arrancando = estado 
        if (self.arrancando):
            print("Arrancando")
        else:
            print("No se pudo arrancar")
    def estado1(self):
        print("El largo es: {}, el ancho es: {}, y el estado de arranque es: {}".format(self.largo,self.ancho,self.arrancando))
class Moto(Vehiculo):
    hacercab = ""
    def caballito(self):
        self.hacercab = "Haciendo el caballito"
    def estado2(self):
        print("El largo es: {}, el ancho es: {}, y el estado de arranque es: {}, {}".format(self.largo,self.ancho,self.arrancando,self.hacercab))

class Velectrico(Vehiculo):
    def __init__(self):
        self.bateria = 100
    
    def estado3(self):
        print("cargado al {}".format(self.bateria))

class AutoFuturo(Velectrico,Vehiculo):
    pass

miMoto = Moto()
miMoto.caballito()
miMoto.estado1()

print("_"*20)

tesla = AutoFuturo()
tesla.bateria=90
tesla.largo=40
print(tesla.largo)
tesla.estado1()
tesla.estado3()

