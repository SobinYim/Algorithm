ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    a,b=map(int,input().split()) #정삼각형 A,B의 한 변의 길이
    res=(a//b)**2 #a//b가 1씩 늘어날 수록 필요한 정삼각형 B의 개수가 공차가 2인 등차수열을 이루므로
    ans.append(f"#{t} {res}")
for a in ans:
    print(a)