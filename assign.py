import pandas as pd
datanya=pd.read_csv("iris.data",
names=["Sepal_Length","Sepal_Width","Petal_Length","Petal_Width","Class"])
ubah_data=datanya.assign(var_baru=datanya['Sepal_Width']+
datanya['Petal_Width'])
print(ubah_data.head(3))