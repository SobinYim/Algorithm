ans=[] #한 번에 출력하기 위한 리스트
T=int(input())
for t in range(1,T+1):
    d,l,n=map(int,input().split()) #기본 데미지, 공격의 레벨, 타격 횟수
    res=sum(range(100,100+l*n,l))*d//100 if l!=0 else d*n #데미지 보너스의 합계에 기본 데미지를 더하고 100을 기준으로 했으므로 100으로 나눔
    ans.append(f"#{t} {res}")
for a in ans:
    print(a)