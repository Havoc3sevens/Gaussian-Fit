#This function is the downhill method used for regression
    #Created by: Enrique Hurtado
    #Date: 04 January 2021
    #Latest update: 04 January 2021
    #History:
        #Date: 01/04/21 || Mod: Program written          || By: Enrique Hurtado
        #Date: 01/04/21 || Mod: Translation from Fortran || By: Enrique Hurtado
        #Date: 01/06/21 || Mod: Translation continued    || By: Enrique Hurtado
        #Date: 01/11/21 || Mod: Beta                     || By: Enrique Hurtado
        #Date: 01/11/21 || Mod: Fixed np array           || By: Enrique Hurtado
    #Purpose: To be used as a prototype, to campare to the Fotran code
        #Specification: Will be supplimented with CPP code
    #Notes: Proof of concept
import math as mt
import numpy as np
from my_lib import*

def downhill(func,xstart,fstart,stepi,epsf,itmin,iters):
    alph=1.0; gamm=2.0; rho=0.5; sig=0.5
    xi = [xstart]; fi = [fstart]
    n = len(xstart)

    for i, value in enumerate(xstart):
        xi.append(xi[0][:])
        xi[i+1][i] = value *(1+stepi)
        fi.append(func(xi[i+1][:]))

    for it in range(iters):

        #ordering
        iter_f = [(v,i) for i,v in enumerate(fi)]
        iter_f.sort()
        f, rank = zip(*iter_f)
        f = list(f)

        x = [ ]
        for i in rank:
            x.append(xi[i][:])
        
        xi = x; fi = f

        #central
        x0 = (np.sum(x[:-1][:], axis= 0)/n)

        if itmin < it:
            deltaf = f[n-1] - f[0]
            if deltaf < epsf:
                #print (it)
                break
        
        xr = x0 + alph*(x0-x[n])
        fxr = func(xr)
        if (fxr < f[n-1]) & (f[0] <= fxr):
            xi[n] = xr
            fi[n] = fxr
            continue

        elif fxr < f[0]:
            xe = x0 + gamm*(x0-x[n])
            fxe = func(xe)
            if (fxe < fxr):
                xi[n] = xe
                fi[n] = fxe
                continue
            else:
                xi[n] = xr
                fi[n] = fxr
                continue
            
        elif fxr >= f[n-1]:
            xc = x[n] + rho*(x0-x[n])
            fxc = func(xc)
            if (fxc <= f[n]):
                xi[n] = xc
                fi[n] = fxc
                continue
            else:
                for i in range(n):
                    xi[i+1] = x[0] + sig*(np.array(x[i+1])-x[n])
                    fi[i+1] = func(xi[i+1])
                continue
    
    return (xi[0], fi[0])