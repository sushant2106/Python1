#Handling Binary Data

#read image and video files 



# f1=open('tiger.jpg','rb')
# f2=open('newpic.jpg','wb')

# bytes=f1.read()
# f2.write(bytes)

# print('new image is availbale')

#read csv module 

#to avoide new line like end=''
import csv
# with open('emp.csv','w',newline='') as f:
#     w=csv.writer(f) #returns csv writter object poinitng of f
#     w.writerow(["ENO","ENAME","EADDRESS"])
#     n=int(input("Enter the no o Emply:"))
#     for i in range(n):
#         eno=int(input("Enter the EMployee Number:"))
#         ename=input("Enter employee Name:")
#         eadd=input("Enter the address:")
#         w.writerow([eno,ename,eadd])


#read data from csv 

f=open("emp.csv",'r')
r=csv.reader(f) #return reader object
print(r)
print(type(r))
data=list(r)

print(data)
print(type(data))

for line in data:
    for word in line:
        print(word,"\t",end='')
        


