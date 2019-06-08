class Persona:
    def __init__(self,dedos,manos):
        self.dedos = dedos
        self.manos = manos
    
    def morfologia(self):
        print("Una persona tiene {} dedos y {} manos".format(self.dedos,self.manos))

class Militar(Persona):
    def __init__(self,dedos,manos,nombre,rango):
        super().__init__(dedos,manos)
     
        self.nombre = nombre
        self.rango = rango

    def estadoRango(self):
        return "El rango de {}, es {}".format(self.nombre,self.rango)

    def morfologia(self):
        super().morfologia()
        
pepe = Militar(2,3,4,5)
print(pepe.estadoRango())
pepe.morfologia()
