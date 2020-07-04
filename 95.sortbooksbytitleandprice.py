print("script to sort books according to title ")
l=eval(input('Enter list of books'))
class Book:
 def setBook(self,l):
    self.d1={}
    self.d2={}
    for x in l:
        print("Enter title for book",x)
        t=eval(input())
        self.d1.update({x:t})
    for x in l:
        print('Enter price of book',x)
        p=eval(input())
        self.d2.update({x:p})
 def sortbytitle(self):
     d={}
     i=0
     l=[]
     for x in self.d1.values():
         l.append(x)
     l.sort()
     while i!=len(l):     
       for x in self.d1.keys():
         if self.d1[x]==l[i]:
             d.update({x:l[i]})
             i+=1
             if i==len(l):
                 break
     print("sort by title:\nBook title price")
     for x in d.keys():
         for y in self.d2.keys():
             if x==y:
                 print(x,'  ',d[x],'  ',self.d2[x])
                 break
 def sortbyprice(self):
     d={}
     i=0
     l=[]
     for x in self.d2.values():
         l.append(x)
     l.sort()
     while i!=len(l):     
       for x in self.d2.keys():
         if self.d2[x]==l[i]:
             d.update({x:l[i]})
             i+=1
             if i==len(l):
                 break
     print("sort by price:\nBook title price")
     for x in d.keys():
         for y in self.d1.keys():
             if x==y:
                 print(x,'  ',self.d1[x],'  ',d[x])
                 break
b=Book()
b.setBook(l)
b.sortbytitle()
b.sortbyprice()
input()
