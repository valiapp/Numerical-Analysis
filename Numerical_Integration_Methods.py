def left_rectangle_rule(f, a, b, h = 0.0001):

    if h == b - a:
        return f(a)*(b - a)
    elif h > (b - a):
        raise Exception("Error! Step size must be less than (b - a)")
    else:
        x = a
        integral = 0

        while x < b:
            integral += h * f(x)
            x += h
    
    return integral


def right_rectangle_rule(f, a, b, h = 0.0001):

    if h == b - a:
        return f(b)*(b - a)
    elif h > (b - a):
        raise Exception("Error! Step size must be less than (b - a)")
    else:
        x = a+h
        integral = 0

        while x <= b:
            integral += h * f(x)
            x += h

    return integral
    

def trapezoidal_rule(f, a, b, h = 0.0001):

    if h == b - a:
        return (f(a)+ f(b))*(b-a)/2
    elif h > (b - a):
        raise Exception("Error! Step size must be less than (b - a)")
    else:
        x = a
        sums = f(a)

        while x <= (b - h):
            x += h
            sums += 2 * f(x)

        sums += f(x)

        return (h/2 * sums)


def simpson_rule(f, a, b, h = 0.0001):

    if h == b - a:
        return (1/3 * (b - a)/2 * (f(a) + 4 * f((a+b)/2) + f(b)))
    elif h > (b - a):
        raise Exception("Error! Step size must be less than (b - a)")
    else:

        sums = f(a)
        x = a + h/2

        sums += 4*f(x)

        while x < (b - h):

            x += h/2
            sums += 2 * f(x)
            x += h/2
            sums += 4 * f(x)

        sums += f(x+h/2)

        return (h/6 * sums)