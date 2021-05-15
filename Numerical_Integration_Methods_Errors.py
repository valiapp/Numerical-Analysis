import numpy as np

def rectangle_rule_error(f_first_derivative, a, b, h):
    z = np.linspace(a,b)

    if h == b - a:
        return ((b-a)**2)/2*max(abs(f_first_derivative(z)))
    elif h > (b - a):
        raise Exception("Error! Step size must be less than (b - a)")
    else:
        return h/2*(b-a)*max(abs(f_first_derivative(z)))

def trapezoidal_rule_error(f_second_derivative, a, b, h):
    z = np.linspace(a,b)

    if h == b - a:
        return (-(b-a)**3)/12*max(abs(f_second_derivative(z)))
    elif h > (b - a):
        raise Exception("Error! Step size must be less than (b - a)")
    else:
        return (h**2/12)*(b-a)*max(abs(f_second_derivative(z)))

def simpson_rule_error(f_fourth_derivative, a, b, h):
    z = np.linspace(a,b)

    if h == b - a:
        return -(((b-a)/2)**5)/90*max(abs(f_fourth_derivative(z)))
    elif h > (b - a):
        raise Exception("Error! Step size must be less than (b - a)")
    else:
        return ((h/2)**4)/180*(b-a)*max(abs(f_fourth_derivative(z)))