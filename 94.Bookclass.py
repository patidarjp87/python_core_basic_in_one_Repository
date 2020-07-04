print("define a class book to stoe book related info like bookid,title,price,author,publisher also define related functions")
class Book:
    def setBook(self):
        bid,t,p,an,pn=[eval(x) for x in input('Enter bookid,title,price,authorname,publisher as it is as you want to see in your script by using separator comma ').split(',')]
        self.bookid=bid
        self.title=t
        self.price=p
        self.author=an
        self.publisher=pn
    def showBook(self):
        print('Books information is :::\nBook id =',self.bookid,'\ntitle =',self.title,'\nprice=',self.price,'\nAuthor name is',self.author,'and publisher name is ',self.publisher)
    def changePrice(self):
        self.price=eval(input('Enter a new price'))
        print("New price of the book is ",self.price)
b=Book()
b.setBook()
b.showBook()
b.changePrice()
input()
