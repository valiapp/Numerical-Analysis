from Differential_Equation_Method import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

F = lambda t, x: np.array([1.1 * x[0] - 0.4*x[0]*x[1], 0.4*x[0]*x[1] - 0.1*x[1]])
x0 = np.array([ 20 , 1 ])
t0 = 0
tmax = 200
dt = 0.01
t, x = euler(F, x0, t0, tmax, dt)

plt.figure()
plt.plot(t, x[:, 0], "b-", t, x[:, 1], "r--")
plt.grid()
plt.title("Time Evolution of Foxes Population and Rabbits Population")
plt.legend(["Rabbits Population", "Foxes Population"])
plt.xlabel("Time")
plt.ylabel("No. of Rabbits and No. of Foxes")

plt.figure()
plt.plot(x[:, 0], x[:, 1], "k--")
plt.grid()
plt.title("Phase Plot")
plt.xlabel("Rabbits Population")
plt.ylabel("Foxes Population")

plt.show()