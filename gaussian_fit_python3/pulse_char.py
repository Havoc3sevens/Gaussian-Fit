"""#########################################################""""""##
 # \file
# Module name: pulse_char.py
 #
 # Copyright 2021 DRS Daylight
 #
 # First written on 01/25/2021 by Enrique Hurtado
 #
 # Module Description:
 #   This module find the frequency and duty cycle of
 #   gausian type signals
 #
 #
 # Below is the script version, the release version is different
 # Revision History:
 #
 #   01/25/21 - Version 0.0.0 - Program put together
 #   01/25/21 - Version 1.0.0 - Alpha Tested
 #
 #############################################################"""

"""#########################################################################""""""#
#  Include Files
#############################################################################"""
import os, sys
import matplotlib.pyplot as plt
from my_lib import*
from readfile import*
from gaussian_lib import*
from downhill_lib import*

def least2(param, plot_gen = False):
    a = param[0]
    b = param[1]
    y1 = param[2]
    x1 = param[3]
    sig1 = param[4]
    y2 = param[5]
    x2 = param[6]
    sig2 = param[7]

    ss = 0.0
    for i in range(minsp, maxsp):
        fi = a*xx[i] + b + y1*mt.exp( -0.5*((xx[i]-x1)/sig1)**2.0 ) + y2*mt.exp( -0.5*((xx[i]-x2)/sig2)**2.0 )
        ss = ss + 1.0/mt.sqrt(yy[i]+2.0) * (yy[i]-fi )**2
    
    ss = ss/abs(maxsp-minsp)

    X = fill_list_nrange(xx[minsp], xx[maxsp], 1000)
    Y = []

    for x in X:
        Y.append(a*x + b + y1*mt.exp( -0.5*((x-x1)/sig1)**2.0 ) + y2*mt.exp( -0.5*((x-x2)/sig2)**2.0 ))
    
    if plot_gen == True:
        plt.plot(xx,yy, color = 'black')
        plt.plot(X,Y, color = 'blue')
        data_out = open('data.csv', 'w+')
        for i in range(len(Y)):
            data_out.write(str(X[i]) + ', ' + str(Y[i]) + '\n')
        data_out.close()
    else:
        pass

    return ss

fname = 'data25.txt'

xx, yy = xy_file(fname)

scan_index = scan_pulses(xx, yy)

norm_y = fill_list_nrange(0,1,len(yy))

y_param = []
x_param = []
sig_param = []
for pulse in scan_index:
    start_scan_i = pulse[0]
    end_scan_i = pulse[1]
    x_in = xx[start_scan_i:end_scan_i]
    y_in = yy[start_scan_i:end_scan_i]
    y1, x1, sig1 = approx_pulse_params(x_in, y_in)
    y_param.append(y1); x_param.append(x1); sig_param.append(sig1)

xstart = [0.0, 0.01, y_param[0], x_param[0], sig_param[0], y_param[1], x_param[1], sig_param[1]]
minsp = 0
maxsp = 45

fstart = least2(xstart)

itmin = 200
iters = 2000
epsf = 0.001
stepi = 0.1
xi, fi = downhill(least2,xstart,fstart,stepi,epsf,itmin,iters)

ffinal = least2(xi, plot_gen = True)
plt.show()

period = xi[6] - xi[3]
frequency = 1.0/period

fwhm1 = 2.0*mt.sqrt(2.0*mt.log(2))*xi[4]
fwhm2 = 2.0*mt.sqrt(2.0*mt.log(2))*xi[7]

duty1 = fwhm1/period
duty2 = fwhm2/period
duty = (duty1 + duty2)/2.0

print duty*100, xi[4], xi[7]
print frequency


