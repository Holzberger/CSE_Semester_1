import numpy as np
from matplotlib import pyplot

knotes = np.array([0, 1, 4])
values = np.array([0, 2, 8])

p = np.polyfit(knotes, values, 2)
print(p)
p = np.polyval(p, 2)

print(p)
input("Press Enter to continue...")

def neville_scheme(knotes, f, x):

    n = len(knotes)

    p = np.zeros((n,n))

    for k in range(n):
        for i in range(n-k):
            if k == 0:
                p[k, i] = f[i]
            else:
                p[k, i] = ((x - knotes[i+k])*p[k-1, i] - (x - knotes[i])*p[k-1, i+1])/(knotes[i]-knotes[i+k])

    return p


knotes = np.array([0, 1, 4])
values = np.array([0, 2, 8])
x = 3

p = neville_scheme(knotes, values, x)
print(np.transpose(p))
input("Press Enter to continue...")

def f(h):
    return (np.exp(h) - 1)/h

I = 10
knotes = np.empty(I)
values = np.empty(I)

for i in range(I):
    knotes[i] = np.exp2(-i)
    values[i] = f(knotes[i])

p = neville_scheme(knotes, values, 0)
p = np.transpose(p)
print(np.transpose(p))

input("Press Enter to continue...")

pyplot.loglog(knotes[0:I], abs(p[0:I,0]-1))
pyplot.loglog(knotes[0:I-1], abs(p[0:I-1,1]-1))
pyplot.loglog(knotes[0:I-2], abs(p[0:I-2,2]-1))

pyplot.show()