print('static member name conflict')
class Base:
    def f1(self):
        Base.x=10
        self.x=1
    def showBase(self):
        print(Base.x)
class Derived(Base):
    x=20
    def f1(self):
        super().f1()
        self.x=2
    def showDerived(self):
        print(Derived.x)
'''d=Derived()
b=Base()
Base.f1(5)
print(Derived.__dict__)
print(Base.__dict__)
print(Base.x)
print(Derived.x)'''
b=Base()
d=Derived()
d.f1()
print(Derived.__dict__)
print(Base.__dict__)
print(Base.x)
print(Derived.x)
print(b.x)
print(Base.x)
print(d.x)
d.showDerived()
d.showBase()
