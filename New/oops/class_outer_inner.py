class Outer:
    def m1(self):
        print('outer class method')
    
    class Inner:
        def m2(self):
            print("Inner class method")


#first way
o=Outer()
o.m1()
i=o.Inner()
i.m2()

#or
#2nd way
x=Outer().Inner()
x.m2()

#3rd
Outer.Inner().m2()



