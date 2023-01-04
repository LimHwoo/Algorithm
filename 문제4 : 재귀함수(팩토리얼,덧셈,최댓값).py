############### 팩토리얼
def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)

################덧셈

def fact_sum(n):
    if n==0:
        return 0
    return n+fact_sum(n-1)

  
################ 최댓값

def find_max(a,n):
    if n==1:
        return a[0]
    max_num = find_max(a,n-1)
    if max_num > a[n-1]:
        return max_num
    else:
        return a[n-1]
