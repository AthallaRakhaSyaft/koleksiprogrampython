import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

def fit_to_window():
    # Mengambil ukuran jendela
    width = root.winfo_width()
    height = root.winfo_height()

    # Mengubah ukuran plot sesuai dengan ukuran jendela
    fig.set_size_inches(width/100, height/100)

    # Memperbarui tampilan plot
    canvas.draw()

# Membuat jendela Tkinter
root = tk.Tk()
root.title("Fit Plot to Window")

# Membuat plot
fig, ax = plt.subplots()
x = np.linspace(0, 10, 100)
y = np.sin(x)
ax.plot(x, y)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Sinusoidal Plot')

# Menyisipkan plot ke dalam jendela Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill=tk.BOTH, expand=True)

# Menambahkan tombol "Fit to Window"
fit_button = tk.Button(root, text="Fit to Window", command=fit_to_window)
fit_button.pack(side=tk.BOTTOM)
 
# Menampilkan jendela
root.mainloop()
