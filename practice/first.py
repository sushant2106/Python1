from sqlalchemy import create_engine,Column,Integer,String,or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


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
cust=session.query(Customers)

for x in cust:
   print(x.name)

