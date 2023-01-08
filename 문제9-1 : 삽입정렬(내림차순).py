def sort_max(a):
    for i in range(1,len(a)):
        value = a[i]
        j = i-1
        while j>=0 and a[j] < value:
            a[j+1] = a[j]
            j = j-1
        a[j+1] = value
    return a
