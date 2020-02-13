import matplotlib.pyplot as plot
import numpy as np
import getpass
host = getpass.getuser()

m = float(input("m: "))
n1 = float(input("n1 = "))
n2 = float(input("n2 = "))
n3 = float(input("n3 = "))
a = float(input("a = "))
b = float(input("b = "))
color = input("color (red/blue/yellow.../hexadecimal value): ")
print("\nA .png file is saved to your desktop")

th = np.arange(0,(2*np.pi), 0.001)
with np.errstate(all='ignore'):
    r = (abs(np.cos((m*th)/4)/a)**n2 + abs(np.sin((m*th)/4)/b)**n3) ** (-1/n1)
    y = r * np.sin(th)
    x = r * np.cos(th)

ax = plot.subplot(111)
ax.grid(False)
ax.axis("off")
ax.plot(x,y, color = color)
plot.gca().set_aspect('equal')
plot.savefig("c:\\Users\\{}\\Desktop\\superformula.png".format(host))
