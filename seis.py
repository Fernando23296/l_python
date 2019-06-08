#primer ejemplo de caso de uso de super

class Animal():
	def __init__(self,ojos,boca):
		self.ojos = ojos
		self.boca = boca

class Humano(Animal):
	def __init__(self,ojos,boca,piernas,brazos):
		super().__init__(ojos,boca)
		self.piernas = piernas
		self.brazos = brazos

pepe=Humano(2,3,4,5)
print(pepe.piernas)
print(pepe.ojos)