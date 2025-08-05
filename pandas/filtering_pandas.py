import pandas as pd 
pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',85)



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

filt= (df['last']=='Doe')
print(df[filt])
print(df[~filt])

#or better do this
print('\n Alternative way to do it')
print(df[df['last']=='Doe'])

#no multiple filteration
print('\n mulitple filter')
print(df[(df['last'] == 'Doe') & (df['first']=='John')])
