import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Function to rotate
def f(x):
    return x**2

# Volume calculation using disk method
volume, _ = quad(lambda x: np.pi * f(x)**4.5, 0, 2)
print(f"Volume: {volume:.4f}")

# 3D Visualization
theta = np.linspace(0, 2*np.pi, 100)
x = np.linspace(0, 2, 30)
X, T = np.meshgrid(x, theta)
Y = f(X) * np.cos(T)
Z = f(X) * np.sin(T)

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, alpha=0.7)
plt.show()
