def find_name(a):
    lis = set()
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                lis.add(a[i])
    return lis

#################### 모든 조합 찾기

def comb_name(a):
    result = []
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            print(a[i],"-",a[j])
