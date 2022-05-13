import pandas as pd


pd.set_option('display.max_columns', None)
pd.set_option('max_columns', None)

data = pd.read_csv('train.csv', delimiter=',')

names = data['Name'].tolist()
found_names=dict()
for i in range(len(names)):
    name = names[i].split(',')[1].split('.')[1].split(' ')
    for nam in name:
        nam = nam.replace(')','').replace('(','')
        if len(nam)==0:
            continue
        if nam in found_names:
            found_names[nam]+=1
        else:
            found_names[nam]=1
names_list =list(found_names.items())
names_list.sort( key=lambda x : x[1])
for i in range(10):
    print(f"{names_list[-i-1][0]} - {names_list[-i-1][1]} times")