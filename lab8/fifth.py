import pandas as pd


pd.set_option('display.max_columns', None)
pd.set_option('max_columns', None)

data = pd.read_csv('train.csv', delimiter=',')


columns_have_null =[]

for column in data:
    if data[column].isnull().values.any():
        columns_have_null.append(column)
print(f'{columns_have_null=}')
print('Filling age')
data['Age'] = data['Age'].fillna(data['Age'].median())
print(data.isnull().any())