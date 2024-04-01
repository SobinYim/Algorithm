T=int(input()) #tc 개수
for t in range(1,T+1):
    n,m=map(int,input().split()) #두 집합의 원소의 개수
    a=set(input().split()) #첫 번째 집합의 원소 문자열
    b=set(input().split()) #두 번째 집합의 원소 문자열
    res=len(a.intersection(b)) #set의 intersection으로 교집합
    print(f"#{t}",res)