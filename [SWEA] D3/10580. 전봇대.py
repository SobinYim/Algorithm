#sol
T=int(input()) #tc 개수
for t in range(1,T+1):
    n=int(input()) #전선의 개수
    li=[] #전선 리스트
    res=0 #교차점 개수 초기화
    for _ in range(n):
        a,b=map(int,input().split()) #전봇대 a와 b의 끝점
        for i,j in li: #전선의 양 끝점 a, b가 다른 점 i, j와 교차하려면 1) a<i, b>j 이거나 2) a>i, b<j 이어야 함
            if (a<i)!=(b<j): #(a<i)!=(b<j)으로 일종의 xor 연산을 구현
                res+=1
        li.append((a,b))
    print(f"#{t}",res)

#sol2
T=int(input()) #tc 개수
for t in range(1,T+1):
    n=int(input()) #전선의 개수
    li=[] #전선 리스트
    res=0 #교차점 개수 초기화
    for i in range(n):
        t1,t2=map(int,input().split()) #전봇대 a와 b의 끝점
        mx=max(t1,t2)
        mn=min(t1,t2)
        if i!=0:
            res+=sum(map(lambda p: (mn<p[1]<=p[0]<mx) or (p[1]<mn<=mx<p[0]) or (p[2]!=(t1<t2) and ((p[1]<=mx<=p[0]) or p[1]<=mn<=p[0])),li)) #경우의 수
        li.append((mx,mn,t1<t2))
    print(f"#{t}",res)

'''
sol2가 처음에 제출한 코드이고, sol이 정리하면서 다시 제출한 코드
sol은 a와 b 각각의 전봇대의 끝점끼리 비교하고 이를 xor 연산으로 방향이 다르다면 카운트하였음
처음에 제출했을 때는 교차점이 생기는 경우의 수를 if문으로 카운트하는 방식을 사용했는데, 최댓값 최솟값을 사용하고 전선의 방향으로 판단했음
그런데 경우의 수를 하나하나 검사하는 게 비효율적으로 느껴져서 해당 경우의 수가 나오기 위한 조건으로 다시 짰다

제출일 기준 python 실행시간 12위, 코드길이 4위(sol)
'''