class Person:
    def __init__(self):
        print('Person Constructor')
        self.name='Durga'
        self.db=self.Dob()

    def display(self):
        print('Name:',self.name)
    
    def display(self):
        print('Name:',self.name)
    
    class Dob:
        print('DOB Class Constructor')
        def __init__(self):
            self.dd=28
            self.mm=5
            self.yy=1948
        
        def display(self):
            print('Dob={self.dd}/{self.mm}/{self.yy}')

p=Person()
p.display()
p.db.display()

##################

class Human:
    def __init__(self):
        self.name='Sunny'
        self.head=self.Head()
        self.brain=self.Brain()
    
    def display(self):
        print('Hello',self.name)
    
    class Head:
        def talk(self):
            print('Talking...')
    
    class Brain:
        def think(self):
            print("Thinking...")



h=Human()
h.display()
h.head.talk()
# h.Head().talk()

h.brain.think()

        


