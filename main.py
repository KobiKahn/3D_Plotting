import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

X1, Y1, Z1 = [], [], []
def scatter_3d(x, y, z, n_range):

    for n in range(n_range):
        z.append(.1 * n * math.pi)
        x.append(math.cos(z[n]))
        y.append(math.sin(z[n]))

    fig = plt.figure(1)  # open a figure for the plot
    ax = fig.add_subplot(111, projection='3d')  # define the axes to 3 dimensional
    ax.plot(x, y, z, '-r*')  # plot the data
    ax.set_xlabel('cos(z))')  # label the x-axis
    ax.set_ylabel('sin(z))')  # label the y-axis
    ax.set_zlabel('z')  # label the z-axis
    ax.set_title('A Helix')
    plt.show()

# scatter_3d(X1, Y1, Z1, 100)

X2 = np.arange(-5, 5, .1)
Y2 = np.arange(-5, 5, .1)
X2_mesh, Y2_mesh = np.meshgrid(X2, Y2)
Z2 = np.cos(X2_mesh) * np.sin(Y2_mesh) * np.tan(X2_mesh + Y2_mesh)
# print(Z2)
# Z2 = np.exp(-(X2_mesh**2 + Y2_mesh**2)/2)

def surface_3d(x, y, z):
    fig = plt.figure(2)
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x,y,z,linewidth=0, antialiased=True,color='aquamarine')
    plt.show()

# surface_3d(X2_mesh, Y2_mesh, Z2)


X3 = np.arange(-5, 5, .1)
Y3 = np.arange(-5, 5, .1)
X3_mesh, Y3_mesh = np.meshgrid(X3, Y3)
Z3 = np.exp(-(X3 ** 2 + Y3 ** 2) / 2.0)
title_3 = 'Wire Frame of z = exp(-(x**2 + y**2)/2.0)'

def wire_3d(x, y, z, title):
    fig = plt.figure(3)
    ax = fig.subplot(111, projection='3d')
    ax.plot_wireframe(x, y, z, rstride=10, cstride=10)
    ax.set_xlabel('X Axis')  # label the x-axis
    ax.set_ylabel('Y Axis')  # label the y-axis
    ax.set_zlabel('Z Axis')  # label the z-axis
    ax.set_title(title)
    plt.show()

wire_3d(X3_mesh, Y3_mesh, Z3, title_3)

