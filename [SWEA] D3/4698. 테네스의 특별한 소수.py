#sol
n=10**6+1 #tc에 들어올 수 있는 최댓값+1
p=[1]*n #에라토스테네스의 체
p[0],p[1]=0,0 #0,1 제외
for i in range(2,n):
    if p[i]==1:
        for j in range(2*i,n,i):
            p[j]=0
T=int(input()) #tc 개수
for t in range(1,T+1):
    d,a,b=input().split() #테네스가 좋아하는 숫자, a 이상 b 이하의 수
    li=[i for i in range(int(a),int(b)+1) if p[i]==1] #a 이상 b 이하의 소수
    res=sum(map(lambda x: d in str(x),li)) #테네스가 좋아하는 숫자가 들어있는 소수의 개수
    print(f"#{t}",res)

#sol2
n=10**6+1 #tc에 들어올 수 있는 최댓값+1
p=[1]*n #에라토스테네스의 체
p[0],p[1]=0,0 #0,1 제외
for i in range(2,n):
    if p[i]==1:
        for j in range(2*i,n,i):
            p[j]=0
T=int(input()) #tc 개수
for t in range(1,T+1):
    d,a,b=input().split() #테네스가 좋아하는 숫자, a 이상 b 이하의 수
    res=0
    for i in range(int(a),int(b)+1):
        if p[i]==1 and d in str(i): #a<=i<=b인 i가 소수이고, 특별한 수가 포함되어 있으면 카운트
            res+=1
    print(f"#{t}",res)

'''
sol2는 sol의 방법에서 li와 res 두 리스트를 만드는 게 메모리를 많이 차지하는 것 같아서 두 과정을 한 번에 합치고,
res를 리스트의 참 값을 합산하는 방법 대신에 조건에 맞을 경우 1씩을 더하는 방식으로 바꾸었다 

제출일 기준 python 코드길이 1위
'''