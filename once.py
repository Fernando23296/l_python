class A():
    def __init__(self,uno,dos):
        self.uno = uno 
        self.dos = dos
    def imprimA(self):
        print("esto es imprim de A, el valor de {} y el valor de {}".format(self.uno,self.dos))

class B():
    def __init__(self,tres,cuatro):
        self.tres = tres
        self.cuatro = cuatro
    
    def imprimB(self):
        print("esto es imprim de B, el valor de {} y el valor de {}".format(self.tres,self.cuatro))

class C(B,A):
    def __init__(self,uno,dos,tres,cuatro):
        self.uno = uno
        self.dos = dos
        self.tres = tres
        self.cuatro = cuatro
        

    def todo(self):
        print("esto es el valor de B: ",self.tres,self.cuatro)

letra = C(1,2,3,4)

letra.todo()
letra.imprimA()
letra.imprimB()
print(C.__mro__)