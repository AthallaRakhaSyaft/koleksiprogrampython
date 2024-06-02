import pandas as pd
dataku=pd.read_csv("data_nilai.csv",names=["Nama","Nilai"])
print(dataku.describe())