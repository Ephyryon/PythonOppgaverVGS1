import numpy as np
import matplotlib.pyplot as plt

def f(A, k, x, c):
    return A*np.sin(k*x+c)

def g(A2, k2, x, c2):
    return A2*np.sin(k2*x+c2)
A=float(input("Skriv verdi for A: "))
k=float(input("Skriv verdi for k: "))
c=float(input("Skriv verdi for c: "))

A2=float(input("Skriv verdi for A2: "))
k2=float(input("Skriv verdi for k2: "))
c2=float(input("Skriv verdi for c2: "))

fig=plt.figure()
ax1=fig.add_subplot(111)
ax1.grid(True)

x=np.linspace(0,8*np.pi,1000)
plt.ylim(-10,10)

ax1.plot(x, f(A,k,x,c))
ax1.plot(x, g(A2,k2,x,c2))

plt.show()