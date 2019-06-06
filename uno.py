class Coche():
	largoCoche = 50
	anchoCoche = 20
	encendido = False 

	def arrancar(self):
		self.encendido = True

	def estado(self):
		if(self.encendido):
			return "Esta encendido"
		else:
			return "Esta apagado"

miCoche = Coche()
print(miCoche.largoCoche)
#miCoche.arrancar()
print(miCoche.estado())
