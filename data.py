import pandas as pd


df = pd.read_csv("data.csv")

del df['hyperlink']
del df['temp_planet_date']


df = df.rename({
    'pl_hostname': 'solarsystem_name',
    'pl_discmethod' : 'planet_discoverymethod'

}, axis = 'columns')




df.to_csv('newdata.csv')



