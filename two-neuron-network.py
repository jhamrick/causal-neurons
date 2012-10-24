# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np

# <codecell>

nsteps = 100
axx = 1.
axy = 2.
ayx = .2
ayy = 1.

# <codecell>

zx = np.random.randn(nsteps) / 2.
zy = np.random.randn(nsteps) / 2.

wxx = -20.
wxy = 1.
wyx = -0.5
wyy = -10.

xv = np.zeros(nsteps)
xxd = np.zeros(nsteps)
xyd = np.zeros(nsteps)
x = np.zeros(nsteps)

yv = np.zeros(nsteps)
yxd = np.zeros(nsteps)
yyd = np.zeros(nsteps)
y = np.zeros(nsteps)

# <codecell>

plt.figure(1)
plt.clf()
plt.subplot(221)
plt.xlim(0, nsteps-1)
plt.ylim(-1, 1)
plt.plot(np.arange(nsteps), zx, 'k')
plt.subplot(222)
plt.xlim(0, nsteps-1)
plt.ylim(-1, 1)
plt.plot(np.arange(nsteps), zy, 'k')
plt.subplot(223)
plt.xlim(0, nsteps-1)
plt.ylim(-1, 1)
plt.subplot(224)
plt.xlim(0, nsteps-1)
plt.ylim(-1, 1)
plt.show()
plt.draw()
plt.draw()

# <codecell>

for t in xrange(nsteps-1):
    xv[t+1] = zx[t] + xxd[t] + yxd[t]
    yv[t+1] = zy[t] + xyd[t] + yyd[t]

    sl = slice(max(0, t-10), t+1)
    nt = x[sl].size - 1
    xf = np.nonzero(x[sl] == 1)[0]
    yf = np.nonzero(y[sl] == 1)[0]
    xxd[t+1] = wxx*np.sum(np.exp(-axx*(nt-np.nonzero(x[sl] == 1)[0])))
    yxd[t+1] = wyx*np.sum(np.exp(-ayx*(nt-np.nonzero(y[sl] == 1)[0])))
    xyd[t+1] = wxy*np.sum(np.exp(-axy*(nt-np.nonzero(x[sl] == 1)[0])))
    yyd[t+1] = wyy*np.sum(np.exp(-ayy*(nt-np.nonzero(y[sl] == 1)[0])))
    
    if xv[t] > 0.5 and yv[t] > 0.5:
        xfirst = np.random.rand() > 0.5
        print xfirst
    else:
        xfirst = True
    
    if xv[t] > 0.5 and xfirst:
        x[t+1] = 1
        xv[t+1] = 0

    elif yv[t] > 0.5:
        y[t+1] = 1
        yv[t+1] = 0

    # print t
    # print z[t]
    # print xd[t+1], xv[t+1], x[t+1]
    # print yd[t+1], yv[t+1], y[t+1]
    # print

    tv = [t, t+1]
    plt.subplot(223)
    plt.plot(tv, x[t:t+2], 'r-')
    plt.plot(tv, xv[t:t+2], 'r--')
    plt.subplot(224)
    plt.plot(tv, y[t:t+2], 'b-')
    plt.plot(tv, yv[t:t+2], 'b--')
    plt.draw() 


# <codecell>

x

# <codecell>

 

