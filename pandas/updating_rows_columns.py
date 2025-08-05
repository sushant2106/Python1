import pandas as pd

pd.set_option('display.max_columns',100)
pd.set_option('display.max_rows',100)

people = {
    "first": ["Corey", "Jane", "John"],
    "last": ["Schafer", "Doe", "Doe"],
    "email": [
        "CoreyMSchafer@gmail.com",
        "JaneDoe@email.com",
        "JohnDoe@email.com"
    ]
}

df=pd.DataFrame(people)
print(df.columns)

#column_rename

df.columns=['first_name','last_name','email']

print(df)

df.columns=[x.lower() for x in df.columns]

df.columns=df.columns.str.replace('_',' ')
print(df)

#only some column 

df.rename(columns={'first_name':'first','last_name':'last'},)

#column rename
df.loc[2]=['john','Smith','jhonsmith@gmail.com']


df.loc[2,['last','email']]=['Doe','jhonsmith@gmail.com']


df.loc[2,'last']='Smith'


print('Filtering the data..')
filt=(df['email']== 'jhonsmith@gmail.com')
# print(df[filt])
# df[filt]['last']=
# print(df)

df.loc[filt,'last']='smith'

print(df['email'].str.lower())

df['email']=df['email'].str.lower()

print(df['email'].apply(len))


if __name__=='__main__':
    pass