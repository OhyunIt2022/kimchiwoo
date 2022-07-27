print("hello world")
print("진행할 작업을 선택해주세요")
print("1. 메모 읽기 2. 메모하기")

option=input()
print(option)
if option=='1':
    print("아직")
elif option=='2':
    f=open('memo.txt')
    memo=f.read()
    print(memo)
else :
    print("잘못 입력함")