
# d=dict()
# d[100]='durga'
# d[200]='shiva'
# print(d)

# print(d[100])

# print(d[400])

d={101:'durga',102:'ji'}

print(d.get(101))
print(d.get(103))
print(d.get(105,0))

# d[101]='Jai durga MAA'
# print(d[101])
# print(d)
# d[104]='RAM JI'
# print(d)

# del d[101]
# print(d)
# d.clear()
# print(d)


# li=['ram','shyam']
# di={100:li}
# print(di)
# #del d we can't use d anymore

# dk=dict()
# dm=dict([(100,'durga'),(200,'ravi'),(300,'shiva')])
# dm2=dict({(100,'durga'),(200,'ravi'),(300,'shiva')})

# print(dm)
# print(dm2)

# print(len(dm2))


# dn=dict(((100,'durga'),(200,'ravi')))
# print(dn)


# print(dn.keys())

# for x in dn.keys():
#     print(x)

# for k,v in dn.items(): print(k,v)




# # dn.pop(100) 
# dn.popitem() #last item htata hai

# dn.setdefault(105,'Maa')

# #agar key rhta  hai toh value nahi replace hoga m
# # magar k nahi hai toh add krndege key and value setdeafult(k,v) 
# print(dn)

# d3={106:'ram'}
# dn.update(d3)
# print(dn)

# print(dn.values())
# print(dn.keys())

# # print(dn.get(1000))



# # d=eval(input("Enter the dictionary:"))
# # s=sum(d.values())
# # print("The Sum:",s)


s='mississippi'

v={'a','e','i','o','u'}
di=dict()

# for x in s:
#     if di.get(x):
#         di[x]+=1
#     else:
#         di.setdefault(x,1)

# for x in s:
#    di[x]=di.get(x,0)+1
# #    print(x,':',di[x])

# for k,v in sorted(di.items()):
#    print('No of %s  occurnace %i' %(k,v))
  
# print(di)

for x in s:
    if x in v:
        di[x]=di.get(x,0)+1
    

print(di)

#comprehension 


squares={x:x*x for x in range(1,6)}
print(squares)

even={x:x*x for x in range(1,6) if x%2 ==0}
print(even)