import pandas as pd
# import os
# import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("insurance.csv")

df['sex'] = df['sex'].apply({'male':0,'female':1}.get)
df['smoker'] = df['smoker'].apply({'yes':1,'no':0}.get)
df['region'] = df['region'].apply({'northeast':1,'northwest':2,'southwest':3,'southeast':4}.get)

df.corr()

x = df.drop(['charges', 'sex'],axis=1)
y = df.charges
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)
 
lireg = LinearRegression()
lireg.fit(x_train,y_train)

pred = lireg.predict(x_test)
data = {'age':60, 'bmi':23, 'children':5, 'smoker':0 , 'region':4}
index = [0]

cust_df = pd.DataFrame(data, index)
cost_pred = lireg.predict(cust_df)

print("Medical insurance : ", cost_pred)