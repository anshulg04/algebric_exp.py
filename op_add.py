class Complex:
    def __init__(self):
        self.real=0
        self.imag=0
    def set(self,r,i):
        self.real=r
        self.imag=i
    def display(self):
        print(self.real,self.imag)
    def __add__(self,comp):
        c=Complex()
        c.real=self.real+comp.real
        c.imag=self.imag+comp.imag
        return c
c1=Complex()
c1.set(2,3)
c2=Complex()
c2.set(2,4)
c3=Complex()
c3=c2+c1
c3.display()
