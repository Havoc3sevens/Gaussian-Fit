def fill_list_nrange(a,b,n):
    step = float(b-a)/(n-1)
    y = []
    f = a
    for i in range(n):
        y.append(f)
        f += step
    return y