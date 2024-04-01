T=int(input()) #tc 개수
for t in range(1,T+1):
    n=int(input()) #농장 크기
    res=0
    for i in range(n):
        temp=abs((n//2)-n+i+1) #마름모 꼴을 만들기 위한 temp
        c1,c2=(0,n) if temp==0 else (temp,-temp) #temp==0일 때를 제외하고 temp:-temp
        li=list(map(int,list(input())))
        res+=sum(li[c1:c2])
    print(f"#{t}",res)