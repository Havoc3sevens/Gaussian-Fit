import csv
import numpy as np

def fileread(fname):
    data1 = np.loadtxt(fname)
    n = sum(1 for line in open(fname))
    ar1 = np.array(data1)

    return (n, ar1)

def fileread_csv(fname):
    with open(fname) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        x = list(readCSV)
        n = sum(1 for line in open(fname))
        ar1 = np.array(x)

    return (n, ar1)

def readline(f, x, y, delim):
    for line in f:
        x.append(float(line.split(delim)[0]))
        y.append(float(line.split(delim)[1]))

def xy_file(fname):
    x = []
    y = []
    try:
        with open(fname) as f:
            delim = ' '
            readline(f, x, y, delim)
            #print ('space')
    except:
        try:
            with open(fname) as f:
                delim = '\t'
                readline(f, x, y, delim)
                #print ('tab')
        except:
            try:
                with open(fname) as f:
                    delim = ','
                    readline(f, x, y, delim)
                    #print ('comma')
            except:
                try:
                    with open(fname) as f:
                        delim = ';'
                        readline(f, x, y, delim)
                        #print ('semi')
                except:
                    try:
                        with open(fname) as f:
                            delim = ':'
                            readline(f, x, y, delim)
                            #print ('colon')
                    except:
                        print ("Text file delimiters are limited " 
                                "to 'Space', 'Tab', 'Comma', "
                                "';', and ':'.")
                        return ('Try', 'again.')
    return (x, y)

def xy_file_explicit(fname, delim):
    x = []
    y = []
    if delim == 'space':
        d = ' '
    elif delim == 'tab':
        d = '\t'
    elif delim == 'comma':
        d = ','
    elif delim == 'semi':
        d = ';'
    elif delim == 'colon':
        d = ':'
    else:
        print ("Provide a valid delimiter, 'space', 'tab', "
                "'comma', 'semi', or 'colon'.")
        return ('Try', 'again.')
        exit()

    try:
        with open(fname) as f:
            readline(f, x, y, d)
            #print (delim)
        return (x, y)
    except:
        print ("Your delimiter, " + "'" + delim + "'" + ", "
                "is not compatible with your file.")
        return ('Try', 'again.')