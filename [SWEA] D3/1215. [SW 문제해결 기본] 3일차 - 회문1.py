def fn_c(x,n): #회문 탐색 x=문자열, n=찾아야하는 회문의 길이
    t=int(n/2)
    res=0
    for i in range(len(x)-n+1):
        if x[i:i+t]==x[i+n-t:i+n][::-1]:
            res+=1
    return res

for t in range(10):
    n=int(input()) #찾아야 하는 회문의 길이
    li=[] #글자판 초기화
    for i in range(8):
        li.append(input())
    if n==1: #n==1 일 경우, 8*8 판이므로 회문은 64개
        res=[64]
    else:
        res=list(map(lambda x: fn_c(x,n),li)) #행마다 회문 탐색
        res.extend(list(map(lambda x: fn_c(x,n),zip(*li)))) #전치행렬
    print(f"#{t+1}",sum(res))