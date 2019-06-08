#ejemplo sencillo del uso de mro
'''
class Foo():
    foo = 'attr foo of Foo'
    

class Bar():
    foo = 'attr foo of Bar' # esto no se vera, puesto que por orden el foo de Foo está primero
    bar = 'attr bar of Bar'

class FooBar(Bar,Foo):
    foobar = 'attr foobar of FooBar'

fb = FooBar()
print(fb.foo)
print(FooBar.__mro__)
'''
class Foo():
    def __init__(self):
        print ("foo init")
    def hola(self,numero):
        print("hola"*numero)

class Bar():
    def __init__(self):
        print ("bar init")
    def hola(self):
        print("chau")

class FooBar(Foo, Bar):
    def __init__(self):
        print ("foobar init")
        super(FooBar,self).hola(9)

a = FooBar()