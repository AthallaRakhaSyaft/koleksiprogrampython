import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk membuat terrain secara acak
def generate_terrain(size):
    terrain = np.random.rand(size, size)
    return terrain

# Fungsi untuk memplot terrain
def plot_terrain(terrain):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    size = terrain.shape[0]
    x = np.arange(0, size)
    y = np.arange(0, size)
    X, Y = np.meshgrid(x, y)
    
    ax.plot_surface(X, Y, terrain, cmap='terrain')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Elevation')
    ax.set_title('Terrain Plot')
    
    plt.show()

# Ukuran terrain (misal: 50x50)
terrain_size = 50

# Membuat terrain
terrain = generate_terrain(terrain_size)

# Memplot terrain
plot_terrain(terrain)
