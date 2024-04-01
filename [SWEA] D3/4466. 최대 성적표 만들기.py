T=int(input()) #tc 개수
for t in range(1,T+1):
    n,k=map(int,input().split()) #시험을 본 과목 개수, 성적표에 넣어야 하는 과목 개수
    res=sorted(map(int,input().split()),reverse=True)[:k] #내림차순 정렬 후, k개만큼 선택
    print(f"#{t}",sum(res))