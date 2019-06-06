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
