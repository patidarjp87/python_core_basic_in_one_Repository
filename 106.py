print('script to learn multiple and hierarchy inheritance')
class A:
    def __init__(self,a):
        self.a=a
class B(A):
    def __init__(self,b):
        self.b=b
        A.__init__(self,10)
class C(A):
    def __init__(self,c):
        self.c=c
        A.__init__(self,10)
class D(B,C):
    def __init__(self,d):
        self.d=d
        super().__init__(20)
        C.__init__(self,30)
obj=D(40)
obj1=C(50)
print(obj.__dict__)
print(obj1.__dict__)

    
