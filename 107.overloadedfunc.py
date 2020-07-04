class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        print(self.a,other.a)
        return self.a+other.a
    def __add__(self,other):        #overloaded function
        print(self.b,other.b)
        return self.b+other.b
a=A(3,89)
b=A(2,3)
print(a+b)
input()
