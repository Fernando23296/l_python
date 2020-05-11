
class Time():
	def __init__(self):
		self.hour = 11
		self.minute = 59
		self.second = 30



def imprimir(hora):
	print("La hora es {} con {} y {} segundos".format(hora.hour,hora.minute,hora.second))

def add_time(t1,t2):
	suma = Time()
	suma.hour = t1.hour + t2.hour
	suma.minute = t1.minute + t2.minute
	suma.second = t1.second + t2.second
	return suma

inicio = Time()
inicio.hour = 2
inicio.minute = 15
inicio.second = 12

duracion = Time()
duracion.hour = 5
duracion.minute = 15
duracion.second = 20

total = add_time(inicio,duracion)
imprimir(total)