import pandas as pd


pd.set_option('display.max_columns', None)
pd.set_option('max_columns', None)

data = pd.read_csv('train.csv', delimiter=',')
print(data.groupby('Sex').mean())


print(data[["Survived","Embarked"]].groupby("Embarked").mean())
