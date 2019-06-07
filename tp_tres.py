#Operator Overloading
class Calculadora():
	def __init__(self,uno=0,dos=0):
		self.uno = uno
		self.dos = dos
	def __str__(num): #el print lo llama directamente
 	 	return "la suma es {} y {}".format(num.uno,num.dos)

	def __add__(a ,b):#el "+" lo llama directamente
		nuevo = Calculadora()
		nuevo.uno = a.uno + b.uno
		nuevo.dos = a.dos + b.dos
		return nuevo

ejem1 = Calculadora(2,3)
ejem2 = Calculadora(4,5)
print(ejem1+ejem2)