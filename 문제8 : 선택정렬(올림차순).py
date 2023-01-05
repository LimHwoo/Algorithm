################# 선택정렬 1

def find_min_idx(a):
    min_idx = 0
    for i in range(1,len(a)):
        if a[min_idx] > a[i]:
            min_idx = i
    return min_idx


def sort_min(a):
    result = []
    while a:
        min_idx = find_min_idx(a)
        value = a.pop(min_idx)
        result.append(value)
    return result

################### 선택정렬 2

def find_min_idx(a):
    
    for i in range(len(a)-1):
        min_idx = i
        for j in range(i+1,len(a)):
            if a[min_idx] > a[j]:
                a[min_idx] , a[j] = a[j] , a[min_idx]
    return a
