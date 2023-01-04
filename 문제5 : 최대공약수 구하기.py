########################### 단순한 방법

def gcd(a,b):
    i = min(a,b)
    while True:
        if a % i == 0 and b % i ==0:
            return i
        i = i-1
        
        


########### 유클리드함수, 재귀함수를 이용

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
  
  
