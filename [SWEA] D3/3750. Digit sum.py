def ds(x): #digit sum 결과가 한 자리 수가 아니라면 재귀
    x=str(sum(map(int,x)))
    if len(x)==1:
        return x
    else:
        return ds(x)

ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    n=input() #자연수 n
    res=ds(n)
    ans.append(f"#{t} {res}")
for a in ans:
    print(a)