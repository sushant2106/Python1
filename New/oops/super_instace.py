class P:
    a=888
    def m1(self):
        self.a=10



class C(P):
    def __init__(self):
        super().m1()
        print(super().a)
        print(self.a)


c=C()

#instance variable can't acess through 
#super()

class M:
    a=777
    def __init__(self):
        self.b=10
    

class N(M):
    a=888
    def __init__(self):
        super().__init__() #jab constructor call kiya toh 
        #parent class ka b bna usmai 10

        self.b=20
        #yaha ab child class mai bhi bko b=10 rakh diya ye usko override kr dega
        print(self.b)
        print(self.a)
        print(super().a)

c=N()


class M1:
    a=777
    def __init__(self):
        self.b=10
    def m1(self):
        self.b=777
    

class N1(M1):
    a=888
    def __init__(self):
        self.b=20
        print('Before:',self.b)
        super().__init__()
        print('After:',self.b)
        super().m1()
        print(self.b)

c=N1()
