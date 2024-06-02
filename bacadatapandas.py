import pandas as pd
datanya=pd.read_csv("iris.data",
names=["Sepal_Length", "Sepal_Width", "Petal_Length",
"Petal_Width","Class"])
print(datanya.shape)