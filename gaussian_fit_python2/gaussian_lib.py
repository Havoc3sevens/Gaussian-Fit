"""#########################################################""""""##
 # \file
# Module name: gaussian_lib.py
 #
 # Copyright 2021 DRS Daylight
 #
 # First written on 01/26/2021 by Enrique Hurtado
 #
 # Module Description:
 #   This module contains functions that scans data files for 
 #   gausian type signals, and finds characteristics
 #
 #
 # Below is the script version, the release version is different
 # Revision History:
 #
 #   01/26/21 - Version 0.0.0 - Program put together
 #
 #############################################################"""

"""#########################################################################""""""#
#  Include Files
#############################################################################"""
import os, sys
import matplotlib.pyplot as plt
import numpy as np
import math as mt
from readfile import*
from my_lib import*

def scan_pulses(xx, yy):
    scan_index = [ ]

    threshold = sum(yy)/len(yy)

    slope = [ ]

    for i in range(len(yy)):
        if i == 0:
            slope.append(0.0)
        else:
            slope.append((yy[i] - yy[i-1])/(xx[i] - xx[i-1]))

    scan_start_it = 0
    for i in range(scan_start_it, len(yy)): #finds where the first pulse will begin to rise
        if yy[i] > threshold:
            posslope_start_t = xx[i]
            posslope_start_it = i
            break

    while i < len(yy)-1:
        for i in range(posslope_start_it, len(yy)): #finds where the slope becomes negative
            if slope[i] < 0:
                negslope_start_t = xx[i]
                negslope_start_it = i
                break

        for i in range(negslope_start_it, len(yy)): #finds where the pulse stops
            if yy[i] < threshold:
                negslope_end_t = xx[i]
                negslope_end_it = i
                break

        pulse_start_it = negslope_end_it
        for i in range(pulse_start_it, len(yy)): #finds where the new pulse begins
            if yy[i] > threshold:
                newpulse_start_t = xx[i]
                newpulse_start_it = i
                scan_end_t = (posslope_start_t + newpulse_start_t)/2.0
                scan_end_it = (posslope_start_it + newpulse_start_it)/2
                break
            else:
                scan_end_t = xx[i]
                scan_end_it = i

        if abs(scan_end_t-xx[scan_end_it])/xx[scan_end_it] <= 0.1:
            posslope_end_it = scan_end_it
        else:
            print "Something went wrong trying to find the next pulse"
            sys.exit()

        scan_index.append([scan_start_it, scan_end_it])

        start = [xx[scan_start_it]]*len(yy)
        plt.plot(start,yy, color = 'blue')  

        scan_start_it = scan_end_it
        posslope_start_t = newpulse_start_t
        posslope_start_it = newpulse_start_it
    end = [xx[scan_end_it]]*len(yy)
    plt.plot(end,yy, color = 'blue')  
    plt.plot(xx,yy, color = 'black')        
    plt.show()
    return scan_index

def approx_pulse_params(xx, yy):
    #find the peak value
    y0 = max(yy)
    x0 = xx[yy.index(y0)]

    #Integration method
    norm = 0.0

    for i in range(len(xx)-1):
        norm += (xx[i+1]-xx[i])*yy[i+1]

    intgrl = 0.0
    norm_int = [intgrl/norm]
    x = []
    y = []
    for i in range(len(xx)-1):
        intgrl += (xx[i+1]-xx[i])*yy[i+1]
        norm_int.append(intgrl/norm)
        if abs(intgrl/norm-0.5) <= 0.15:
            x.append(intgrl/norm)
            y.append(xx[i+1])

    l = len(x)

    if l == 1:
        wlim = y[0]
    elif l%2 == 0:
        m = l/2
        sl = (y[m]-y[m-1])/(x[m]-x[m-1])
        b = y[m-1]-sl*x[m-1]
        wlim = sl*0.5 + b
    elif l%2 == 1:
        m = (l-1)/2
        sl = (y[m+1]-y[m-1])/(x[m+1]-x[m-1])
        b = y[m]-sl*x[m]
        wlim = sl*0.5 + b

    value_check = 0.30

    value_check_i = 0.0 + value_check
    value_check_f = 1.0 - value_check

    first_bound_list = []
    second_bound_list = []

    count = 0
    for int_val in norm_int:
        first_bound_list.append(abs(int_val-value_check_i))
        second_bound_list.append(abs(int_val-value_check_f))
        count += 1

    first_bound_array = np.array(first_bound_list)
    second_bound_array = np.array(second_bound_list)

    init_w_i = first_bound_array.argmin()
    final_w_i = second_bound_array.argmin()

    init_w_v = xx[init_w_i]
    final_w_v = xx[final_w_i]

    sig = (xx[final_w_i]-xx[init_w_i])/2.0*mt.sqrt(2.0*mt.log(2))

    max_p = [x0]*len(yy)
    init_w_l = [init_w_v]*len(yy)
    final_w_l = [final_w_v]*len(yy)
    max_p = [x0]*len(yy)
    plt.plot(max_p,yy, color = 'green')
    plt.plot(init_w_l,yy, color = 'blue')
    plt.plot(final_w_l,yy, color = 'blue')
    plt.plot(xx,yy, color = 'black')
    plt.show()
    return (y0, x0, sig)