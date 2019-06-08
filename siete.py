class A:
    def say(self): 
    	print("class A")

class B(A):
    def say(self): 
    	print("class B")

class C(A):
    def say(self): 
    	print("class C")

class D(B,C):
    def say(self): 
    	print("class D")

x = D()
super(B, x).say()  # --> class C
print(D.__mro__)