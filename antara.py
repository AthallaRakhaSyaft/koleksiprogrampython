w=int(input("Nilai W:"))
if w==0:
    kalimat="W bernilai nol"
elif w>0 and w<=10:
    kalimat="W di antara 0 dan 10"
elif w>10:
    kalimat="W lebih besar dari 10"
else:
    kalimat="W bernilai negatif"
print(kalimat)    