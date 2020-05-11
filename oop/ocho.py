class Vehiculo():
	def __init__(self,llantas,asientos):
		self.llantas = llantas
		self.asientos = asientos
	def mostrar(self):
		print("El vehiculo tiene {} llantas y {} asientos".format(self.llantas,self.asientos))

class Moto(Vehiculo):
	def __init__(self,tanque,frenos):
		self.tanque = tanque
		self.frenos = frenos

	def caballito(self):
		print("haciendo el caballito")

class Velectrico(Vehiculo):
	def __init__(self,enchufe):
		self.enchufe = enchufe

	def activarSolar(self):
		print("Se activo la energia solar")

class Melectrico(Velectrico,Moto):
	def __init__(self,llantas,asientos,tanque,frenos,enchufe):
		super().__init__(llantas,asientos,tanque,frenos,enchufe)
		self.llantas= llantas
		self.asientos = asientos
		self.tanque = tanque
		self.frenos = frenos
		self.enchufe = enchufe
	

tesla = Melectrico(2,3,4,5,6)
print(tesla.llantas)