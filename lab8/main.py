import pandas as pd


pd.set_option('display.max_columns', None)
pd.set_option('max_columns', None)

data = pd.read_csv('train.csv', delimiter=',')
# print(train)
print('\tMen')
print(data[data["Sex"] == 'male'].groupby('Pclass').mean()[["Survived"]])
print('\n\n\tWomen')
print(data[data["Sex"] == 'female'].groupby('Pclass').mean()[["Survived"]])




