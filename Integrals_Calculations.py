from Numerical_Integration_Methods import *
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

f =  lambda x : np.exp(3*x) * np.sin(2*x)
a = 0 
b = np.pi / 4

left_rectangle_errors = np.zeros(7)
right_rectangle_errors = np.zeros(7)
trapezoidal_errors = np.zeros(7)
simpson_errors = np.zeros(7)
step_size_array = np.array([1e-01, 1e-02, 1e-03, 1e-04, 1e-05, 1e-06, 1e-07])
real_integral = (3/13*np.exp(3*np.pi / 4) + 2/13)

for index, h in enumerate(step_size_array):
    left_rectangle_errors[index] = abs(left_rectangle_rule(f, a, b, h) - real_integral)
    right_rectangle_errors[index] = abs(right_rectangle_rule(f, a, b, h) - real_integral)
    trapezoidal_errors[index] = abs(trapezoidal_rule(f, a, b, h) - real_integral)
    simpson_errors[index] = abs(simpson_rule(f, a, b, h) - real_integral)

plt.figure()
plt.loglog(step_size_array, left_rectangle_errors)
plt.grid(True)
plt.title('Left Rectangle Rule Errors')
plt.xlabel('Step Size')
plt.ylabel('Error')

plt.figure()
plt.loglog(step_size_array, right_rectangle_errors)
plt.grid(True)
plt.title('Right Rectangle Rule Errors')
plt.xlabel('Step Size')
plt.ylabel('Error')

plt.figure()
plt.loglog(step_size_array, trapezoidal_errors)
plt.grid(True)
plt.title('Trapezoidal Rule Errors')
plt.xlabel('Step Size')
plt.ylabel('Error')

plt.figure()
plt.loglog(step_size_array, simpson_errors)
plt.grid(True)
plt.title('Simpson Rule Errors')
plt.xlabel('Step Size')
plt.ylabel('Error')

plt.show()