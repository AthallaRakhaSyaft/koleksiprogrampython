import matplotlib.pyplot as plt

# Membuat data untuk plot
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Membuat outline plot
plt.plot(x, y, color='black', linewidth=2, linestyle='-')

# Menambahkan judul dan label sumbu
plt.title('Outline Plot')
plt.xlabel('X')
plt.ylabel('Y')

# Menampilkan grid
plt.grid(True)

# Menampilkan plot
plt.show()
