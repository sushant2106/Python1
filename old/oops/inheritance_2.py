# class Parent:
#     def show(self):
#         print("I am parent class..")

# class Child(Parent):
#     def show(self):
#         print("I am Child classes...")

# obj=Child()
# obj.show()
# class One:
#     def method_one(self):
#         print("Method one..")
#     def mehtod(self):
#         print("Commin method one")

# class Four:
#     def method_four(self):
#         print("Method Four")

#     def method(self):
#         print("Common Method Four")

# class Two:
#     def method_two(self):
#         print("Method Two")

#     def method(self):
#         print("Common Method Two")

# class Five:
#     def method_two(self):
#         print("Method Five")

#     def method(self):
#         print("Common Method Five")




# class Three(Four,Five,Two,One):
#     pass

# obj=Three()
# # obj.method_one()
# # obj.method_two()

# obj.method()

class A:
    def method(self):
        print("Method of class A")

class B:
    def method(self):
        print("Method of class B...")
class C(A):
    def method(self):
        print("Mehtod of class C")


class D(B,C):
    pass

obj=D()
obj.method()
