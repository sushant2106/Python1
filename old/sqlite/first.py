import sqlite3
from em1 import Employe




conn=sqlite3.connect('emply.db')

c=conn.cursor()

# c.execute(""" CREATE TABLE  if not exists employe(
#           first text,last text,
#           pay integer
# ) """)

# c.execute("INSERT INTO  employe VALUES ('Corey','Schafer',5000)")

emp_1=Employe('Ram','Kumar',80000)
emp_2=Employe('Dr','Sachin',100000000)


#c.execute("INSERT INTO employe VALUES('{}','{}','{}')".format(emp_2.first,emp_2.last,emp_2.pay))


# c.execute("INSERT INTO employe VALUES (?,?,?)",(emp_2.first,emp_2.last,emp_2.pay))

# c.execute("INSERT INTO employe VALUES (:first,:last,:pay)",(emp_1.first,emp_1.last,emp_1.pay))


# c.execute("SELECT * FROM employe")

# print(c.fetchone()[0])


# print(c.execute("SELECT * FROM  employe"))

c.execute("SELECT * FROM  employe WHERE last=?",('Schafer',))

print(c.fetchall())


c.execute("SELECT * FROM  employe WHERE last=:last",{'last':'Sachin'})

print(c.fetchall())

conn.commit()
conn.close()


def insert_emp(emp):

    with conn:
       c.execute("INSERT INTO employe VALUES (?,?,?)",(emp.first,emp.last,emp.pay))



def get_emps_by_name(lastname):
    c.execute("SEELCT * FROM employe WHERE last=:last",{'last':lastname})
    return c.fetchall()

def update_pay(emp,pay):
    with conn:
        c.execute(""" UPDATE employe SET=:pay WHERE first=:first AND last=:last
                    """,{'first':emp.first,'last':emp.last,'pay':emp.pay})
        



