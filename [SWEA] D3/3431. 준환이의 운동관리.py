T = int(input())
for i in range(1,T+1):
    L,U,X=map(int,input().split())
    res=0 if L<=X<=U else -1 if X>U else L-X #L<=X<=U 라면 0, X<L 이라면 L-X, L<X 라면 -1을 반환
    print(f"#{i}", res)