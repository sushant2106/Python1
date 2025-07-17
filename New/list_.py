# # # l=eval(input("Enter the list:"))
# # # print(l)

# # l=list(range(0,10,2))
# # print(l)

# # s='durga ji'
# # l=list(s)
# # print(l)

# # l2=[10,20,[30,40]] #nested list 

# # print(l2[::-1])
# # # print(l2[10])
# # print(l2[2][0])

# # l2[0]=19
# # print(l2)

# # l=[10,20,30,10,20]
# # print(len(l))
# # print(l.count(10))
# # print(l.index(10))
# # target=int(input("Enter the value of search:"))
# # if target in l:
# #     print(target,"available in first occuranc")
# # else:
# #     print("Not avialable..")
# # # print(l.index(50))

# # # x='smaer'
# # # print(x.find('m'))

# # try:
# #     print(target)
# # except ValueError:
# #     print(target,"Not avialble")

# # Manipulating Element
# # x=list()
# # print(type(x))

# # for i in range(101):
# #     if i%10==0:x.append(i)

# # print(x)

# # x.insert(1,50)
# # print(x)
# # x.insert(50,77)
# # print(x[len(x)-1])
# # x.insert(-10,88)
# # print(x)
# # print(x.index(88))
# # # for i in range(0,100,10)

# # l1=["Chickend","Fish"]
# # l2=['c','l']

# # l1.extend(l2)
# # print(l1)
# # l3=l1+l2
# # print(l3)

# # l1=[10,20,30]
# # l2=[40,50,60]
# # l1.extend(l2)
# # l1.extend('durga') #every charcter is cinsider as object
# # l1.append('durga')
# # print(l1)

# # l1=[10,12,20,30,12]
# # l1.remove(12)
# # print(l1)

# # x=int(input("Enter the no:"))
# # if x in l1:
# #     l1.remove(x)
# # else:
# #     print("No...")
# # print(l1.pop())
# # print(l1.pop())
# # print(l1)
# # print(l1.pop(2))

# # print(len(l1))

# # l1=[10,80,30,40]
# # l1.reverse()
# # print(l1)
# # l1.sort()
# # print(l1)

# # l2=["Boy","Apple","Cat"]
# # l2.sort()
# # print(l2)

# # l3=[10,30,40,"apple",'dy']
# # l3.sort()  hetro is not allow only homegenous


# #to sort in reverse alphabetic order

# # l3=[44,56,22,11]
# # l3.sort(reverse=True)
# # print(l3)

# x=[10,20,30,40]
# # y=x

# # x[0]=111
# # print(x,y,sep=',')
# # print(id(x))
# # print(id(y))

# # m=x[::]
# # print(id(m))
# # print(id(x))

# # m=x.copy()
# # print(m)
# a=[1,2,3,4]
# # b=[3,4,56]

# # c=a+b
# # d=a.extend(b)
# # e=a.append(b)
# # print(c)
# # print(a)
# # print(a)

# # c=a*2
# # print(c)
# # print(c.sort())
# # print(c.sort(reverse=True))

# # x=['Dog','cat']
# # m=['cat','Dog']
# # y=['Dog','cat']
# # z=['Dog','Cat']
# # print(x==y)
# # print(x!=y)
# # print(x==z)
# # print(x!=m)
# # print(x is y) #refresnce data ko check kr rha hai

# # <,<=,>,>=

# # x=[11,2,50]
# # y=[11,10,12]

# # # # print(x>y)
# # # # print(y>x)
# # # print(y>=x)

# # print(10 in x)
# # print(100 not in x)

# # x.clear() #remove all the number 
# # print(x)

# # x=[[10,20,30],[40,0,40]]

# # for i in range(len(x)):
# #     for j in range(len(x[i])):
# #         print(x[i][j],end=' ')
# #     print()

# # l1=[]
# # for x in range(1,11):
# #     l1.append(x*x)
# # print(l1)

# l1=[x*x  for x in range(1,11)]
# print(l1)
# # a=2
# # print(a*3)

l1=[x*x for x in range(1,11)]
l2=[x  for x in l1 if x%2 ==0]
print(l2)

l3=[x for x in l2 if x%2 !=0]
print(l3)

l4=[x**2 for x in l2 if (x**2)%2==0]
print(l4)


word=['abc','dessf','ghsjsji']
l5=[w[0] for w in word]
print(l5)
l6=[w for w in word if len(w)>=4]
print(l6)

n1=[10,20,30,40]
n2=[30,40,50,60]

l7=[x for x in n1 if x in n2]
print(l7)

# not in

wor="The quick brown fox jumps over the lazy dog".split()
# print(wor)

l8=[[w.upper(),len(w)]for w in wor]

print(l8)