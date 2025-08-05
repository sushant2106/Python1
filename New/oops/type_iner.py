#single inheritance

class P:
    def m1(self):
        print('Parent MEthod')

class C(P):
    def m2(self):
        print('Child Method')


c=C()
c.m1()
c.m2()

#Multilevel Inheritance 
print('Multilevel Inheritance')

class GF:
    def m1(self):
        print('land')

class F(GF):
    def m2(self):
        print('Cash')
class U(F):
    def m3(self):
        print('Enjoy')
  
u=U()
u.m1()
u.m2()
u.m3()


#Hirearchy Inheritance 
#one to many 
print('Hirearchy Inheritance...')
class P1:
    def m1(self):
        print('Parent..')

class C1(P):
    def m2(self):
        print('Child1')

class C2(P):
    def m3(self):
        print('Child2')

c1=C1()
c1.m1()
c1.m2()

c2=C2()
c2.m1()
c2.m3()
