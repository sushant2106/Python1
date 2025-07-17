# city=input("Enter theCity Name:")
# list=["Hyderabad","Delhi","Mumbai"]

# #lstrip(),rstrip(),"strip()"
# if city.strip() in list:
#     print(city)   
# else:
#     print("Not available")


# x="rnajjjjhb"

# print(x.find("j"))
# print(x.rfind("j"))
# print(x.find("k"))

# s="Learing Python is very easy"

# print(s.find("a"))
# print(s.rfind("a"))
# # print(s.split(' '))

# print(s.find("P",5,10))

# #it gave error when it doesn't have index 
# print(s.index("m",5,10))
    


# s=input("Enter the Main String:")
# subs=input("input sub:")
# try:
#     n=s.index(subs)
# except:
#     print("Substring is notin the main..")
# else:
#     print("Substrign Found")


# s=input("Enter the string:")
# subs=input("Enter the subs:")
# print(s.count(subs))
# print(s.count(subs,8,len(s)))
# flaf=False
# pos=-1
# n=len(s)

# while True:
#     pos=s.find(subs,pos+1,n)
#     if pos == -1:
#         break
#     else:
#         print("found index:",pos)
#         flag=True

# if flag==False:
#     print("Not Found..")

# s="Learning python is very difficult"
# print(id(s))
# s=s.replace("difficult","easy")
# print(id(s))
# print(s)



# s1=10
# print(id(s1))
# del s1

# s="2029-09-101"
# print(s.split("-"))
# print(s.rsplit(''))
# a,b,c=10,20,30
# print(a,b,c,sep='-')

# # txt ="apple#banana#cherry#orange#papaya"
# # x=txt.split("#",3)
# # print(x)

# # print(txt.rsplit('#',3))

# l=['durga','soft','solution']

# s='-'.join(l)
# print(s)

# L2=('durga','soft','solution')
# print(' '.join(L2))

# #change the case of string 

# s='Ram Ji Ki nikali'
# print(s.lower())
# print(s.upper())
# print(s.swapcase()) #upper become lower and vice-versa
# print(s.title())
# print(s.capitalize())


s2='Learning Python is very easy'
# # print(s2.replace('easy','Hard'))
# # print(s2.startswith("easy"))
# # print(s2.endswith("easy"))
# # print(s2.startswith("Learning"))
# print(s2.find("Python"))
# print(s2.split(" "))



# for i in range(len(s2)):
#     print(s2[i],end=' ')

# print('Durga12'.isalnum())
# print('Durga62'.isalpha())
# print('Durga'.isalpha())
# print('Durga65'.isdigit())
# print('abc'.islower())
# print('ABC'.isupper())
# print('abc123'.islower())
# print('ABC123'.isupper())
# print('Learning Python is very easy'.istitle())
# print(' '.isspace())
# print("Durga Soft".isspace())
# print('Is123'.istitle())

# s=input("Enter any Character:")

# if s.isalnum():
#     print("The alpha  is %s" %s)
#     if s.isalpha() and s.islower():
#         print('tHE LOWER')
#     else:
#         print("The Upper")
# elif s.isspace():print(s)
# else:
#     print(s)

# name='durga'
# age=48
# salary=10000
# print("{}'s age is and his salry is {}".format(name,age,salary))
# print("{0} 's sgae is {1} and his salry is {2}".format(name,age,salary))
# print("{x} age is {y} and his slary is {z}".format(x=name,y=age,z=salary))

# s="ram ji ki nikali sawari"
# print(s[::-1])
# print("".join(reversed(s)))
# for i in reversed(s):
#     print(i,end='')

# for i in reversed(s):
#     print(i)

# i=len(s)-1
# out=""
# while i>=0:
#     out+=s[i]
#     i-=1
# print(out)

# input='Durga Software Solutions'
# x= input.split(" ")

# for i  in range(len(x)):
#     s=x[i][ :: -1]
#     print(s)
# print(x)

# l2=[]
# for i in range(len(x),0,-1):
#     l2.append(x[i-1])
#     print(x[i-1])
   

# print(' '.join(l2))

s1='RAVISOFT'
s2='TEJA'
# s3=[]
# i,j=0,0

# while  i<len(s1) or j<len(s2):
#     if i<len(s1):
#         s3.append(s1[i])
#         i+=1
#     if j<len(s2):
#         s3.append(s2[j])
#         j+=1

# print(''.join(s3))
# print(s1[::2])
# print(s1[1::2])
# i=0
# while i<len(s1):
#     print(s1[i],end=',')
#     i+=2

# s=input("Enter Some String:")
# s1=s2=output=''

# for x in s:
#     if x.isalpha():
#         s1+=x
#     else:
#         s2+=x
# print(s1,s2)

# for x in sorted(s1):
#     output+=x

# for x in sorted(s2):
#     output+=x

# # print(output)


# s=input("Enter the String:")
# out=""
# l1=[]
# prev=''
# for x in s:
#     if x.isalpha():
#         out+=x
#         prev=x
#     else:
#         out+=prev*(int(x)-1)

# print(out)

# for x in s:
#     if x.isalpha():
#         out+=x
#         prev=x
#     else:
#         newchar=chr(ord(prev)+int(x))
#         out+=newchar

# print(out)

# for x in s:
#     if x not in l1:
#         l1.append(x)
    
# print(','.join(l1))

s=input("Enter the String:")
# out=""
dict={}

#d.keys() d.itmes()

# d={100:'durga',200:'shiva'}
# # for k,v in d.itmes():
for x in s:
    if x not in dict.keys():
        dict[x]=1
    else:
        dict[x]+=1

# print(dict)

for k,v in dict.items():
    print(k,v)



    
    
    












    

