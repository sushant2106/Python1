from sqlalchemy import create_engine,Column,Integer,String,or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#hi
engine=create_engine('sqlite:///sales.db',echo=True)
Base=declarative_base()

Session=sessionmaker(bind=engine)

session=Session()

class Customers(Base):
   __tablename__ = 'customers'
   id = Column(Integer, primary_key=True)

   name = Column(String)
   address = Column(String)
   email = Column(String)


Base.metadata.create_all(engine)


# cust1=Customers(name="Ram",address="Sikta",email="ram@gmail.com")

# cust2=Customers(name="Sachin",address="Sikta",email="Sachin@gmail.com")

# # session.add(cust1)
# session.add_all([cust1,cust2])
# session.commit()

# cust=session.query(Customers)

# for x in cust:
#    print(x.name)

# cust=session.query(Customers).order_by(Customers.name)
# for x in cust:
#    print(x.name)

##########----get data by filtering----#############

# cust=session.query(Customers).filter(Customers.name=="Sachin").first()
# print(cust.email)

#cust=session.query(Customers).filter(or_(Customers.name=='Sachin',Customers.name=='Ram'))

# cust_count=session.query(Customers).filter(or_(Customers.name=='Sachin',Customers.name=='Ram')).count()
# print(cust_count)