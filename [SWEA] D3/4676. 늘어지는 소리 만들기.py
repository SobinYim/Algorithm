T=int(input()) #tc 개수
for t in range(1,T+1):
    s=list(input()) #초기 문자열
    n=int(input()) #삽입할 하이픈의 개수
    li=list(map(int,input().split())) #하이픈을 넣을 위치
    li=sorted(li,reverse=True) #index가 바뀌지 않도록 뒤에서부터 하이픈을 넣기 위해 내림차순 정렬
    for i in li:
        s.insert(i,"-")
        print(s)
    print(f"#{t}","".join(s))