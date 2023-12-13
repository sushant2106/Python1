import sqlite3

conn=sqlite3.connect('test.db')

# conn.execute(''' CREATE TABLE Student
#           (ID INT  AUTO_INCREMENT PRIMARY KEY NOT NULL,
#         NAME TEXT NOT NULL,
#         AGE  INT NOT NULL);   
# ''')

# ins=''' insert into Student(ID,NAME,AGE) VALUES (3,'Sachin','20')
   
# '''

# conn.execute(ins)

#to retirive 
x=(20,10)
c=conn.cursor()
ret=''' SELECT * FROM Student WHERE AGE IN x;
'''
c.execute(ret)


# for x in c.fetchone():
#     print(x)

# for x in c.fetchall():
#     print(x)

# for x in c.fetchall():
#     print(x[0])

print(c.fetchall())












#conn.commit()
conn.close()