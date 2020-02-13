import matplotlib.pyplot as plot
import numpy as np
import getpass
host = getpass.getuser()

m = float(input("m (=m1=m2): "))
n1 = float(input("n1 = "))
n2 = float(input("n2 = "))
n3 = float(input("n3 = "))
a = float(input("a = "))
b= float(input("b = "))
color = input("color (red/blue/yellow.../hexadecimal value): ")
print("\nA .png file is saved to your desktop")

th = np.arange(0,(2*np.pi), 0.001)
with np.errstate(all='ignore'):
    ro = abs(np.cos((m*th)/4)/a)**n2 + abs(np.sin((m*th)/4)/b)**n3
    r = abs(ro) ** (-1/n1)
    y = r * np.sin(th)
    x = r * np.cos(th)
