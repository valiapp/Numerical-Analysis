import numpy as np

def euler(F, x0, t0, tmax, dt):

    t = np.arange(t0, tmax, dt)
    x = np.zeros( (len(t), len(x0)) )
    x[0,:] = x0 

    for n in range(len(t)-1):
        x[n+1, :] = x[n, :] + dt*F(t[n], x[n, :])

    return t, x