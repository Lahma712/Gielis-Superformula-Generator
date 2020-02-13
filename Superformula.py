import matplotlib.pyplot as plot
import numpy as np
import getpass
host = getpass.getuser()

k = int(input("Number of rounds (k*pi): "))
m1 = eval(input("m1: "))
m2 = eval(input("m2: "))
n1 = eval(input("n1 = "))
n2 = eval(input("n2 = "))
n3 = eval(input("n3 = "))
a = eval(input("a = "))
b = eval(input("b = "))
color = input("color (red/blue/yellow.../hexadecimal value): ")
print("\nA .png file is saved to your desktop")

th = np.arange(0,(k*np.pi), 0.0001)
with np.errstate(all='ignore'):
    r = (abs(np.cos((m1*th)/4)/a)**n2 + abs(np.sin((m2*th)/4)/b)**n3) ** (-1/n1)
    y = r * np.sin(th)
    x = r * np.cos(th)

ax = plot.subplot(111)
ax.grid(False)
ax.axis("off")
ax.plot(x,y, color = color)
plot.gca().set_aspect('equal')

plot.savefig("c:\\Users\\{}\\Desktop\\superformula.png".format(host))
plot.show()
