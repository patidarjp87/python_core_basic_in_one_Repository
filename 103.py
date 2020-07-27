
print('Basics of inheritance')
class person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def showPerson(self):
        print("name =",self.name,'age=',self.age)
class student(person):
    def __init__(self,r,n,a):
        self.rollno=r
        super().__init__(n,a)
    def showStudent(self):
        print('name=',self.name,'age=',self.age,'roll no =',self.rollno)
s1=student(1,'ajay',20)
s2=student(2,'amit',21)
student.__init__(s2,4,'amit',21)
print(s1.__dict__)
print(s2.__dict__)
input()
        
