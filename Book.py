class publisher():
    def __init__(self,pname):
        self.pname=pname
    def display(self):
        print("name:",self.pname)
class Book(publisher):
    def __init__(self,pname,bname,title):
        self.pname=pname
        self.bname=bname
        self.title=title
    def display(self):
        print("Name:",self.pname)
        print("Bname:",self.bname)
        print("title:",self.title)
class Python(Book):
    def __init__(self,pname,bname,title,page,price):
        self.pname=pname
        self.bname=bname
        self.title=title
        self.page=page
        self.price=price
    def display(self):
        print("Name:",self.pname)
        print("Bname:",self.bname)
        print("title:",self.title)
        print("page:",self.page)
        print("Price:",self.price)
n=input("Enter Publisher:")
b=input("Enter Author:")
t=input("Enter Title:")
p=input("Enter Pages:")
pr=input("Enter Price:")
obj=Python(n,b,t,p,pr)
obj.display()
