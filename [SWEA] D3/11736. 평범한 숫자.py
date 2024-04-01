T=int(input()) #tc 개수
for t in range(1,T+1):
    n=int(input()) #길이
    li=list(map(int,input().split())) #수의 리스트
    res=0
    for i in range(1,n-1):
        temp=li[i-1:i+2] #검사할 수열, 해당 회의 수가 최솟값도 최댓값도 아니라면 결과 값에 1을 더함
        if li[i]!=max(temp) and li[i]!=min(temp):
            res+=1
    print(f"#{t}",res)