import matplotlib.pyplot as plot
import numpy as np
import getpass
from PIL import Image
host = getpass.getuser()

k = int(input("Number of rounds (k*pi): "))
m1 = eval(input("m1: "))
m2 = eval(input("m2: "))
n1 = eval(input("n1 = "))
n2 = eval(input("n2 = "))
n3 = eval(input("n3 = "))
a = eval(input("a = "))
b = eval(input("b = "))
color = input("Line color (red/blue/yellow.../#hexadecimal value): ")
colorfill = input("Fill color: ")
print("\nA .png file is saved to your desktop")

theta = np.arange(0,(2*k*np.pi), 0.001)
with np.errstate(all='ignore'):
    r = (abs(np.cos((m1*theta)/4)/a)**n2 + abs(np.sin((m2*theta)/4)/b)**n3) ** (-1/n1)
    y = r * np.sin(theta)
    x = r * np.cos(theta)

graph = plot.subplot(111)
graph.grid(False)
graph.axis("off")
graph.plot(x,y, color = color)
graph.fill(x,y, color = colorfill)

plot.gca().set_aspect('equal')

plot.savefig("c:\\Users\\{}\\Desktop\\superformula.png".format(host))
Image.open("c:\\Users\\{}\\Desktop\\superformula.png".format(host)).show()
