class Coche():

	def __init__(self):
		self.__ancho= 24
		self.__largo= 48
		self.__estado = False

	def enceder(self,arrancar):
		self.__estado = arrancar
		estadoChequeo = self.__chequeo()
		if (self.__estado and estadoChequeo):
			return "Arrancando"
		else:
			return "Parado"
	def __chequeo(self):
		self.motor="ok"
		self.puertas="ok"
		print("Realizando la inspeccion")

		if(self.puertas == "ok" and self.motor=="ok"):
			return True
		else:
			return False 

miCoche = Coche()
print(miCoche.enceder(True))

