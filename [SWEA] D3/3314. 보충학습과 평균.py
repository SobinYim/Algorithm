ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    res=sum(map(lambda x: int(x) if int(x)>39 else 40,input().split()))//5 #점수는 모두 5의 배수이므로 몫으로 계산
    ans.append(f"#{t} {res}")
for a in ans:
    print(a)
