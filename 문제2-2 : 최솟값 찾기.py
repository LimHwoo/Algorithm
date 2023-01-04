def find_min(a):
    min_result = a[0]
    for i in range(1,len(a)):
        if min_result > a[i]:
            min_result = a[i]
    return min_result
