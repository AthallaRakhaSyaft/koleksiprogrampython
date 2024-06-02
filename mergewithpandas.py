# Untuk import dan load data csv
import pandas as pd
nilai_biologi=pd.read_csv("nilai_biologi.csv",names=["NIS","Nama","Nilai_Biologi"])
nilai_matematika=pd.read_csv("nilai_matematika.csv",names=["NIS","Nama","Nilai_Matematika"])
# Untuk melihat shape (baris dan kolom) dari data
print(nilai_biologi.shape)
print(nilai_matematika.shape)
# Untuk melihat daftar nilai Biologi dan nilai Matematika
print("Daftar Nilai Biologi")
print(nilai_matematika)
# Untuk merge dan print hasil merge
gabung=pd.merge(nilai_biologi,nilai_matematika)
print(gabung)