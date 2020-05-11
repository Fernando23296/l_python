#tp = Think Python exercises
class Point():
	pass

blank = Point()
blank.x = 3.0
blank.y = 4.0

def print_point(xd):
	print(xd.x,xd.y)
class Rectangle():
	pass

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def find_center(rect):
	p = Point()
	#Asumiendo que rect es como el tipo box de arriba
	p.x = rect.corner.x + rect.width/2.0
	p.y = rect.corner.x + rect.height/2.0
	return p 

center = find_center(box)
print_point(center)
print("-"*30)
p1 = Point()
p1.x = 3.0
p1.y = 4.0
p2 = p1



import copy
p3 = copy.copy(p1)
p1.x += 9.0
print(p2.x)
print(p3.x)

box2 = copy.copy(box)
#el copy ayuda pero no al nivel embebido (a un nivel mas profundo no)
print(box2.corner==box.corner)
#la solucion es usar deepcopy
box3 = copy.deepcopy(box)
print(box3 is box)
print(box3.corner is box.corner)

'''si no estas seguro de si x atributo es parte del objeto
se usa hasattr
'''
p = Point()
print(hasattr(p,'x'))
print(hasattr(p,'z'))

