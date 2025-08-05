import pandas as pd 
pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',85)

person = {
    "first": "Corey",
    "last": "Schafer",
    "email": "CoreyMSchafer@gmail.com"
}

person = {
    "first": "Corey",
    "last": "Schafer",
    "email": "CoreyMSchafer@gmail.com"
}

people = {
    "first": ["Corey", "Jane", "John"],
    "last": ["Schafer", "Doe", "Doe"],
    "email": [
        "CoreyMSchafer@gmail.com",
        "JaneDoe@email.com",
        "JohnDoe@email.com"
    ]
}


# for x,y in people.items():
#     print(x,y)

# for x in people.keys():
#     print(x)

df=pd.DataFrame(people)
# print(df)

print(df['email'])

# print(df.email)

#to access multiple column

print(df[['last','email']]) #its returning another df

df_new=df[['last','email']]


#to check the column 
print('Columns',df.columns,'\n')

#order to get rows 
print(df.iloc[0]) #access low based on index

print(df.iloc[0,1])

#we can get rows and column both

print('To get Row and column')

print(df.iloc[[0,1],2])


#We can use loc

print(df.loc[0])

#now multiple row
print(df.loc[[0,1]])

#2nd value to specific column 
print(df.loc[[0,1],'last'])

print(df.loc[[0,1],['last','email']])


#how to set_index

df.set_index('email',inplace=True)

print(df)

print(df.iloc[0]) 

#df.reset_index(inplace=True)



