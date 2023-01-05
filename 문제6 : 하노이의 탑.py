def hanoi(n,from_,to_,sub_):
    if n==1:
        return print(from_,"->",to_)
    hanoi(n-1,from_,sub_,to_)
    print(from_,"->",to_)
    hanoi(n-1,sub_,to_,from_)
