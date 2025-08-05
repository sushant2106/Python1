import pandas as pd
pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',85)

df=pd.read_csv('matches - matches.csv')

# print(data)
print(df.head(5))
print(df.tail(5))

print(df.shape)
print(df.shape[0])


print(df.info())  #provide column

print(df.columns)

print(df[['season','city']])
print(df.loc[1,'team1'])

print(df['team1'].value_counts())

print(df.loc[1])


print(df.loc[[0,1,2],['team1','team2']])

#index slicing
#row and column 
print(df.loc[0:2,'team1':'toss_decision'])


#to set index
#df.set_index('team1',inplace=True)

#or 
#df=pd.read_csv('match.csv',index_col='team1')

#to sort index

df.sort_index()
#for permanent sorting 

#df.sort_index(inplace=True)

#filtering win by run 

print('\n Win By Run is')

df_run=df[df['win_by_runs']>10]

print(df_run[['team1','win_by_runs']])



city=['Mumbai','Indore','Delhi']

filt2=df['city'].isin(city)
print(df.loc[filt2,'city'].value_counts())


filt3=df['team1'].str.contains('Royal',na=False)

print(df.loc[filt3])





if __name__ == '__main__':
    pass