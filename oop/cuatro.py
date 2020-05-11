
class Vehiculo():
	def __init__(self):
		self.ancho = 45
		self.largo = 90
		self.arranca = False

	def arrancar(self,estado):
		self.arranca = estado
		if (self.arranca):
			return "ya esta arrancando"
		else:
			return "aun no"

#Moto hereda de Vehiculo
class Moto(Vehiculo):
	pass

moto1 = Moto()
print(moto1.largo)