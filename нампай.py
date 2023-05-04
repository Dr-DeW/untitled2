import pandas as pd

data = {
    'apples':[1,2,3,5],
    'orange':[2,3,52,63]
}
p = pd.read_csv('IMDB-Movie-Data.csv',index_col='Title')
p2 = p.append(p)
p2.drop_duplicates(inplace=True, keep='first')
p2.rename(columns={
'Runtime (Minutes)': 'RunTime',
'Revenue (Millions)':'Revenue'
}, inplace=True)
p2.columns = [col.lower() for col in p2]
#p2.dropna(axis=1, inplace=True)
re = p2['revenue']
re_mean = re.mean()
re.fillna(re_mean, inplace=True)

gen_col = p2[['genre','rating']]
prom = p2.loc['Prometheus':'Sing']
con = (p2['director']=='Ridley Scott')
#print(p2[(p2['rating']>=8.6) | (p2['director']=='Ridley Scott')])

#print(p2[p2['director'].isin(['Christopher Nolan',"Ridley Scott"])])
def rating_f(x):
    if x >=8.0:
        return 'good'
    else: return 'bad'

p2['rating_category'] = p2['rating'].apply(rating_f)
print(p2.head(2))


