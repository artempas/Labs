import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from random import randint

pd.set_option('display.max_columns', None)
pd.set_option('max_columns', None)

train = pd.read_csv('train.csv', delimiter=',')
train['Age'] = train['Age'].fillna(train['Age'].median())
test = pd.read_csv("test.csv", delimiter=',')
test['Age'] = test['Age'].fillna(test['Age'].median())
train = train.dropna()
test = test.dropna()

print("Percentage of females who survived:", train["Survived"][train["Sex"] == 'female'].mean())
print("Percentage of males who survived:", train["Survived"][train["Sex"] == 'male'].mean())
print('-' * 100)
print("Percentage of Pclass = 1 who survived:", train["Survived"][train["Pclass"] == 1].mean())
print("Percentage of Pclass = 2 who survived:", train["Survived"][train["Pclass"] == 2].mean())
print("Percentage of Pclass = 3 who survived:", train["Survived"][train["Pclass"] == 3].mean())
print('-' * 100)
print("Percentage of SibSp = 0 who survived:", train["Survived"][train["SibSp"] == 0].mean())
print("Percentage of SibSp = 1 who survived:", train["Survived"][train["SibSp"] == 1].mean())
print("Percentage of SibSp = 2 who survived:", train["Survived"][train["SibSp"] == 2].mean())
print('-' * 100)
print("Percentage of Parch = 0 who survived:", train["Survived"][train["Parch"] == 0].mean())
print("Percentage of Parch = 1 who survived:", train["Survived"][train["Parch"] == 1].mean())
print("Percentage of Parch = 2 who survived:", train["Survived"][train["Parch"] == 2].mean())
print("Percentage of Parch = 3 who survived:", train["Survived"][train["Parch"] == 3].mean())
print("Percentage of Parch = 4 who survived:", train["Survived"][train["Parch"] == 4].mean())
print("Percentage of Parch = 5 who survived:", train["Survived"][train["Parch"] == 5].mean())
print('-' * 100)
print("Percentage of Age <25 who survived:", train["Survived"][train["Age"] < 25].mean())
print("Percentage of Age [25;50] who survived:", train["Survived"][50 >= train["Age"]][train["Age"] >= 25].mean())
print("Percentage of Age 50+ who survived:", train["Survived"][50 < train["Age"]].mean())
print('-' * 100)

sex_mapping = {"male": 0, "female": 1}
train['Sex'] = train['Sex'].map(sex_mapping)
test['Sex'] = test['Sex'].map(sex_mapping)
embarked_mapping = {"S": 1, "C": 2, "Q": 3}
train['Embarked'] = train['Embarked'].map(embarked_mapping)
test['Embarked'] = test['Embarked'].map(embarked_mapping)

predictors = train.drop(['Survived', 'PassengerId', 'Name', 'Ticket', 'Fare', "Cabin"], axis=1)
target = train["Survived"]
x_train, x_val, y_train, y_val = train_test_split(predictors, target, test_size=0.22, random_state=0)
decisiontree = DecisionTreeClassifier()
decisiontree.fit(x_train, y_train)
y_pred = decisiontree.predict(x_val)
acc_decisiontree = round(accuracy_score(y_pred, y_val) * 100, 2)
print(acc_decisiontree)

test['Survived'] = decisiontree.predict(test[['Pclass', "Sex", 'Age', 'SibSp', 'Parch', 'Embarked']])
print(test.head())
for line in test.iterrows():
    for item in line:
        print(line, '\n\n')
