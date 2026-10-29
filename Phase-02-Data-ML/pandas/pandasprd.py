import pandas as pd
import numpy as np


#  Pandas Series  
data = np.array(['g','e','e','k','s'])
s = pd.Series(data)

print('Pandas Series : ')
print(s)

# Pandas DataFrame

# # Working with rows and columns in pandas dataframe

data = {"Name": ['Jai','Princi','Gaurav','Anuj'],
        'Age':[27,30,28,35],
        'Address':['Delhi','Kanpur','Allahabad','Kannauj'],
        'Qualification':['Msc','MA','MCA','PHD']
        } 
df = pd.DataFrame(data)
print(df[['Name', 'Qualification']])


dta = pd.read_csv("nba.csv", index_col="Name")
first = dta.loc["Avery Bradley"]
second = dta.loc["R.J. Hunter"]
print(first, "\n\n\n", second)


# Operations in pandas

df = pd.read_csv("data-.csv")
print(df.head())

df.info()

ages = df[df['age'] > 25]
print(ages)
