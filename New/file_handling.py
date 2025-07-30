# f=open('abc.txt','w')
# # f=open('abcddd.txt','x') exclsuive mode
# print("file name",f.name)
# print("file mode",f.mode)
# print("is file Readable?",f.readable())
# print("is Writable",f.writable())
# print("is file Closed",f.closed)
# f.close()
# print("is file Close",f.closed)


#writing data to the text files

#f=open(filename,mode)
#r,w,a,r+,w+,a+,x
#binary -> rb,wb,ab,r+b,w+b,a+b

f2=open('abcd.txt','w')

# f2=open('abcd.txt','a')
f2.write('durga\n')
f2.write('writen \n')
list=['sunny\n','Bunney\n','Vinny\n']
#write multiline
f2.writelines(list)
print("ducssfully done")


