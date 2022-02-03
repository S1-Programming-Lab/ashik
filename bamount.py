class bank():
    def __init__(self,acnt,name,typ,amt):
        self.ac=acnt
        self.nam=name
        self.type=typ
        self.amount=amt
    def printamt(self):
        print("anct name=",self.nam)
        print("anct num=",self.ac)
        print("anct type=",self.type)
        print("bal=",self.amount)
    def withl(self,wl):
        return(self.amount-wl)
n=input("enter name:")
t=input("enter type")
a=int(input("enter numbr:"))
am=int(input("enter amount:"))
obj=bank(a,n,t,am)
print("account details")
obj.printamt()
w=int(input("enter amount to withdraw:"))
print("bl=",obj.withl(w))
