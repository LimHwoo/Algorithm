################# 삽입정렬 1
def find_idx(sorted_list,value):
    for i in range(len(sorted_list)):
        if value < sorted_list[i]:
            return i
    return len(sorted_list)

def sort_min(a):
    result = []
    while a:
        value = a.pop(0)
        idx = find_idx(result,value)
        result.insert(idx,value)
    return result

################## 삽입정렬 2

def sort_min(a):
    for i in range(1,len(a)):
        j = i-1
        value = a[i]
        while j>=0 and a[j] > value:
            a[j+1] = a[j]
            j = j-1
        a[j+1] = value
    return a
  
  
