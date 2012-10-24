# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#############
## Imports ##
#############

import numpy as np
import matplotlib.pyplot as plt

# <codecell>

###############
## Constants ##
###############

TIMESTEP   =  1    # length of time for each step, ms
REST_POT   = -70   # membrane resting potention, mV
AP_THRESH  = -55   # action potential threshold, mV
AP_POT     =  40   # action potential peak, mV

# <codecell>

################
## Parameters ##
################

nsteps = 100     # number of time steps to run simulation for

rd     = 50.0    # refractory inhibition decay rate, mV / ms
axy    =  2.0    # X->Y synaptic potential decay rate, mV / ms
ayx    =  0.5    # Y->X synaptic potential decay rate, mV / ms

wd     = -115.0  # refractory inhibition weight
wxy    =  50.0   # X->Y synaptic weight
wyx    = -25.0   # Y->X synaptic weight

# <codecell>

########################
## Specify input data ##
########################

zx = np.random.randn(nsteps) * 10
zy = np.random.randn(nsteps) * 10

# <codecell>

######################################
## Allocate arrays for network data ##
######################################

# pre-threshold values for each neuron
xv = np.zeros(nsteps) + REST_POT
yv = np.zeros(nsteps) + REST_POT

# post-threshold vlaues for each neuron
x = np.zeros(nsteps)
y = np.zeros(nsteps)

# potential decay for each synapse
xxd = np.zeros(nsteps)
xyd = np.zeros(nsteps)
yxd = np.zeros(nsteps)
yyd = np.zeros(nsteps)

# <codecell>

#########################
## Initialize plotting ##
#########################

# plotting parameters
ylim = (-100, 100)
xlim = (0, nsteps-1)
nrow = 4
ncol = 2

def create_subplot(ix):
    ax = plt.subplot(nrow, ncol, ix)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.grid(True)
    if ((ix-1) % ncol) != 0:
        ax.set_yticklabels([])
    if (nrow*ncol - (ix-1)) > ncol:
        ax.set_xticklabels([])
    return ax

# create figure
plt.close('all')
fig = plt.figure(1)
plt.clf()
fig.set_figwidth(8)
fig.set_figheight(10)

# x input
ax_zx = create_subplot(1)
ax_zx.plot(np.arange(nsteps), zx, 'k')
# y input
ax_zy = create_subplot(2)
ax_zy.plot(np.arange(nsteps), zy, 'k')
# x value (pre-threshold)
ax_xv = create_subplot(3)
# y value (pre-threshold)
ax_yv = create_subplot(4)
# x value
ax_x = create_subplot(5)
ax_x.set_ylim(-0.05, 1.05)
# y value
ax_y = create_subplot(6)
ax_y.set_ylim(-0.05, 1.05)
# x potential decay
ax_xd = create_subplot(7)
# y potential decay
ax_yd = create_subplot(8)

# <codecell>

for t in xrange(nsteps-1):

    # update pre-threshold values
    xv[t+1] = zx[t] + xxd[t] + yxd[t] + REST_POT
    yv[t+1] = zy[t] + xyd[t] + yyd[t] + REST_POT

    # generate an action potential, if necessary
    if xv[t] > AP_THRESH and yv[t] > AP_THRESH:
        xfirst = np.random.rand() > 0.5
        print xfirst
    else:
        xfirst = True
    
    if xv[t] > AP_THRESH and xfirst:
        x[t+1] = 1
        xv[t] = AP_POT
        xv[t+1] = REST_POT

    elif yv[t] > AP_THRESH:
        y[t+1] = 1
        yv[t] = AP_POT
        yv[t+1] = REST_POT

    # update post-threshold membrane potential for each neuron 
    sl = slice(max(0, t-10), t+1)
    nt = x[sl].size - 1
    xf = np.nonzero(x[sl] == 1)[0]
    yf = np.nonzero(y[sl] == 1)[0]

    xxd[t+1] = wd*np.sum(np.exp(-(rd*TIMESTEP)*(nt-np.nonzero(x[sl] == 1)[0]))) 
    yyd[t+1] = wd*np.sum(np.exp(-(rd*TIMESTEP)*(nt-np.nonzero(y[sl] == 1)[0])))

    yxd[t+1] = wyx*np.sum(np.exp(-(ayx*TIMESTEP)*(nt-np.nonzero(y[sl] == 1)[0])))
    xyd[t+1] = wxy*np.sum(np.exp(-(axy*TIMESTEP)*(nt-np.nonzero(x[sl] == 1)[0])))

    # plotting
    tv = [t, t+1]
    ax_xv.plot(tv, xv[t:t+2], 'r-')
    ax_x.plot(tv, x[t:t+2], 'r-')
    ax_xd.plot(tv, xyd[t:t+2], 'r-')
    ax_yv.plot(tv, yv[t:t+2], 'b-')
    ax_y.plot(tv, y[t:t+2], 'b-')
    ax_yd.plot(tv, yxd[t:t+2], 'b-')

plt.show()

# <codecell>

 

# <codecell>


