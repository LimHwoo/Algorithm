######################## 숫자가 존재하는 모든 인덱스 반환
def search(input_num,find_num):
    result = []
    for i in range(len(input_num)):
        if find_num == input_num[i]:
            result.append(i)
    return(result)
