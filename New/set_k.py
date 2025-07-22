# s={13,10,3,5,23}
# print(s)

# l1=[102,39,22]
# print(set(l1))

# m=set('durga')
# print(m)

# print(set(range(1,19,4)))

# s=set()
# print(type(s))

# st={}
# print(type(st))


#importnat method  of set 

# s={10,20,30}

# s=set()
# s.add(10)
# s.add(20)
# s.add(30)
# s.add(40)

# print(s)
# l=[11,23,14]
# s.update(l)
# print(s)
# #add take only one argument while update take any no of argument
# s.update(range(1,11,4),l,'durgaa')
# print(s)
# s.add('Python')
# print(s)


# l1=[222,122]
# l2=l1.copy()
# print(l2,id(l1),id(l2))
# s2=s.copy()
# print(s2)
# print(s.pop())
# print(l1.pop())
# print(len(s))

# print(s.remove('a'))
# print(l1.remove(222))
# s.remove(140)

# print(s.discard(140))

# s.clear()
# s.add(1)
# print(s)

# s1={10,20,30,40}
# s2={30,40,50,60}
# print(s1.union(s2)) #s1 | s2
# print(s1|s2)
# print(s1.intersection(s2)) # s1 & s2

# print(s1.difference(s2)) #s1-s2 a new set with elements that are in the first set but not in the second.
# print(s1-s2)

# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# print(A.symmetric_difference(B))
# print(A^B)

# s1=set('durga')
# print(s1)


# s={x*x for x in range(1,6)}
# s.add(22)
# print(s)

l=eval(input("Enter the some list:"))
s=set(l)
print(s)


w=input("Enter some word:")
s=set(w)
v={'a','e','i','o','u'}
d=s.intersection(v)

print(d)



