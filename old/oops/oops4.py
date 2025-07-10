class Animals:
	def __init__(self):
		self.legs = 4
		self.domestic = True
		self.tail = True
		self.mammals =True

	def isMammal(self):
		if self.mammals:
			print("It is a mammal.")
		else:
		    print("No")

	def isDomestic(self):
		if self.domestic:
			print("It is a domestic animal.")

class Dogs(Animals):
    def __init__(self):
        super().__init__()
 
    def isMammal(self):
        super().isMammal()
        
x=Dogs()
x.isMammal()