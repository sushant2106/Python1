import sqlite3

conn=sqlite3.connect("sqlite.db")

# conn.execute('''
#     Create table student (
#      st_id INT AUTO_INCREMENT PRIMARY KEY,
#      st_name VARCHAR(50),
#      st_class VARCHAR(10),
#      st_email VARCHAR(30)
             
#     )
# ''')

# conn.close()

# ins='''
#   insert into student(st_name,st_class,st_email) VALUES('ram','ECE','ram@gmial.com')
# '''
# conn.execute(ins)
# conn.commit()
# conn.close()

data=conn.execute("select * from student")

for n in data:
    print(n)

# conn.close()