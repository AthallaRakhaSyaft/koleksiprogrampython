import matplotlib.pyplot as plt
import numpy as np

x = np.array([40, 20, 25, 15])
labelku = ["Kelas X-A", "Kelas X-B", "Kelas X-C", "Kelas X-D"]
warnaku = ['saddlebrown', 'gold', 'lightblue', 'mediumorchid']

fig, ax = plt.subplots()
ax.pie(x, labels=labelku, colors=warnaku, autopct='%1.d%%')
ax.set_title("Jumlah Peserta Lomba Lari")
plt.show()
