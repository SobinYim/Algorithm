ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    n,m=map(int,input().split()) #이진수로 표현할 수, 해당 수의 마지막 n 비트
    res="ON" if bin(m)[-n:]=="1"*n else "OFF" #m을 이진수로 변환한 결과의 마지막 n비트가 모두 1이라면 "ON"을 아니라면 "OFF"를 할당
    ans.append(f"#{t} {res}")
for a in ans:
    print(a)

'''
bin(num) : 정수를 이진수로 변환
이외에도 oct(8진수), hex(16진수)
int(num, unit)으로 10진수 변환

제출일 기준 python 실행시간 5위
'''