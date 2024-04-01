#sol : math
from math import sqrt,ceil
ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    n=int(input()) #화살의 개수
    res=0 #점수 초기화
    for i in range(n): #화살의 개수만큼 반복
        x,y=map(int,input().split()) #화살의 x,y 좌표
        r=sqrt(x**2+y**2) #피타고라스 정리를 이용해 반지름을 구하고
        p=11-ceil(r/20) #반지름을 점수화
        p=0 if p<0 else 10 if p>10 else p #점수를 0과 10 사이로 정리
        res+=p
    ans.append(f"#{t} {res}")
for a in ans:
    print(a)

#sol2 : filter
ans=[] #한 번에 출력하기 위한 리스트
s=[80000]+[i**2 for i in range(200,0,-20)]+[-1] #점수 당 반지름의 제곱 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    n=int(input()) #화살의 개수
    res=0 #점수 초기화
    r2=[] #반지름의 제곱
    for i in range(n): #화살의 개수만큼 반복
        x,y=map(int,input().split()) #화살의 x,y 좌표
        r2.append(x**2+y**2)
    for i in range(10):
        res+=len(list(filter(lambda x: s[i]>=x>s[i+1],r2)))*i #filter를 이용하여 해당 구간의 값이 몇 개인지 카운트
    ans.append(f"#{t} {res}")
for a in ans:
    print(a)

#sol3 : 점수 list 생성
s=[80000]+[i**2 for i in range(200,0,-20)] #점수 당 반지름의 제곱 리스트
li=[0]*80001 #경우의 수
t=10 #점수, index로 사용
for i in range(s[1]+1): #0점일 경우 더 반복할 필요 없으므로
    if i>s[t]:
        t-=1
    li[i]=t
ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    n=int(input()) #화살의 개수
    res=0 #점수 초기화
    for i in range(n): #화살의 개수만큼 반복
        x,y=map(int,input().split()) #화살의 x,y 좌표
        res+=li[(x**2+y**2)] #반지름의 제곱을 인덱스로 꺼내온 점수를 합산
    ans.append(f"#{t} {res}")
for a in ans:
    print(a)

'''
local 환경에서 test 시, sol2가 실행 시간이 더 길어 제출하지는 않았다
sol3이 무식하기는 하지만 실행 시간이 가장 빠른 게 좀 재밌다...

제출일 기준 python 코드길이 1위(sol), 실행시간 10위(sol3)
'''