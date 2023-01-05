############# 학생번호와 이름이 리스트로 주어져있을때, 학생 번호를 입력하면 해당 학생 이름을 반환, 없으면 ? 출력

def search_name(stu_no,stu_name,input_no):
    for i in range(len(stu_no)):
        if input_no == stu_no[i]:
            return print(stu_name[i])
    return print("?")
