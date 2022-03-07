class library():
    def __init__(self,regno,place,lname):
        self.reg=regno
        self.pl=place
        self.ln=lname
class openAccount(library):
    def __init__(self,regno,place,lname,name,age,plac):
        self.reg=regno
        self.pl=place
        self.ln=lname
        self.n=name
        self.a=age
        self.p2=plac
    def display(self):
        print("Register number : ",self.reg)
        print("Place : ",self.pl)
        print("Librarian Name : ",self.ln)
        print("Name : ",self.n)
        print("Age : ",self.a)
        print("Place : ",self.p2)
r=input("Enter the register number : ")
p=input("Enter the place : ")
l=input("Enter the Librarian's name : ")
n=input("Enter the name : ")
a=int(input("Enter the age : "))
p2=input("Enter the place : ")
print("\nAccount details\n")
obj=openAccount(r,p,l,n,a,p2)
obj.display()
            
            
