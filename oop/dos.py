
class Coche():
	def __init__(self):
		self.__ancho = 50 #encapsulado
		self.largo = 100
		self.encendido = False

	def arrancar(self,estado):
		self.encendido=estado
		if (self.encendido):
			return "esta encendido"
		else:
			return "no esta encendido"

	def descripcion(self):
		print("El ancho del auto es: ",self.__ancho,"y el largo es: ", self.largo)


miCoche= Coche()
print(miCoche.arrancar(estado=False))
miCoche.ancho=1
miCoche.descripcion()
