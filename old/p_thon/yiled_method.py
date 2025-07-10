def generator():

   yield "Welcome"

#   yield "to"

#   yield "Simplilearn"

gen_object = generator()
print(generator())

# print(type(gen_object))

for i in gen_object:
  print(i)


def odd(number):
   
   for num in range(number):
      if num%2!=0:
         yield num


odd_number=odd(20)
print(type(odd_number))

print(list(odd_number))