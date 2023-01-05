################ 원하는 숫자의 인덱스 반환
def search(into_num,find_num):
    for j in range(len(into_num)):
        if find_num == into_num[j]:
                return j
    return -1
    
