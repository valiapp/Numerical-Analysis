from Numerical_Integration_Methods import *
import numpy as np 
import matplotlib.pyplot as plt

f =  lambda x : np.exp(3*x) * np.sin(2*x)
a = 0 
b = np.pi / 4

left_rectangle_errors = np.array
right_rectangle_errors = np.array
trapezoidal_errors = np.array
simpson_errors = np.array
step_size_array = np.array([1e-01, 1e-02, 1e-03, 1e-04, 1e-05, 1e-06, 1e-07])

for h in step_size_array:
    left_rectangle_errors = np.append(left_rectangle_errors, [left_rectangle_rule(f, a, b, h) - (3/13*np.exp(3*np.pi / 4) + 2/13)])
    right_rectangle_errors = np.append(right_rectangle_errors, [right_rectangle_rule(f, a, b, h) - (3/13*np.exp(3*np.pi / 4) + 2/13)])
    trapezoidal_errors = np.append(trapezoidal_errors, [trapezoidal_rule(f, a, b, h) - (3/13*np.exp(3*np.pi / 4) + 2/13)])
    simpson_errors = np.append(simpson_errors, [simpson_rule(f, a, b, h) - (3/13*np.exp(3*np.pi / 4) + 2/13)])