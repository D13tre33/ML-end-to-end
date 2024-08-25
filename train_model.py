import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import joblib

Fraud_data = pd.read_csv('creditcard.csv')
Fraud_data.head()
Fraud_data.tail()
Fraud_data.info()

Fraud_data.isnull().sum()

Fraud_data['Class'].value_counts()
legit = Fraud_data[Fraud_data.Class == 0]
fraud = Fraud_data[Fraud_data.Class == 1]

print(legit.shape)
print(fraud.shape)

legit.Amount.describe()
fraud.Amount.describe()

RANDOM_SEED = 42
LABELS = ["legit", "fraud"]
count_classes = pd.value_counts(Fraud_data['Class'], sort = True)
count_classes.plot(kind = 'bar', rot=0)
plt.title("Transaction Class Distribution")
plt.xticks(range(2), LABELS)
plt.xlabel("Class")
plt.ylabel("Frequency")

Fraud_data.groupby('Class').mean()

# randomly select 492 legit transactions to match the 492 fraudulent transactions
# to make a even distribution
legit_sample = legit.sample(n=492)

new_data = pd.concat([legit_sample, fraud], axis = 0)
new_data.head()
new_data.tail()

new_data['Class'].value_counts()
new_data.groupby('Class').mean()

x = new_data.drop(columns= 'Class', axis = 1)
y = new_data['Class']

print(x)
print(y)

x_train, x_test, y_train, y_test =train_test_split(x, y, test_size=0.2, stratify = y, random_state=2)
print(x.shape, x_train.shape, x_test.shape)

model = LogisticRegression()
model.fit(x_train, y_train)

x_train_prediction = model.predict(x_train)
training_data_accuracy = accuracy_score(x_train_prediction, y_train)

x_test_prediction = model.predict(x_test)
test_data_accuracy = accuracy_score(x_test_prediction, y_test)

print('Accuracy score on Test Data : ', test_data_accuracy)

# Save the trained model
joblib.dump(model, 'model.joblib')
