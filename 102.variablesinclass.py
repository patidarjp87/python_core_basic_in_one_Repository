class test :
    a=19
    def __init__(self):
        self.x=1
        test.b=20
    def  f1(self):
        x=100
        self.x=2
        test.c=30
    def f2():
        y=200
        test.d=40
    @staticmethod
    def f3(m):
        test.e=50
        m.y=3
    @classmethod
    def f4(cls,s):
        cls.f=60
        test.g=70
        s.z=4
test.h=80
t1=test()
#t.f1()
#test.f1(test)
#test.f1(t)
#test.f1(test)
#test.f2()
#t.f3(test)
#test.f3(t)
#t.f4(t)
#test.f4(test)
t2=test()
t1.f3(t2)
t1.f4(t2)
print(test.__dict__)
print(t1.__dict__)
print(test.__dict__)
print(t2.__dict__)
input()
