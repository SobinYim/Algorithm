ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    li=tuple(map(int,input().split())) #Alice와 Bob의 경기 수와 승리 수
    a,b=li[0]/li[1],li[2]/li[3] #Alice와 Bob의 승률
    res="ALICE" if a>b else "DRAW" if a==b else "BOB"
    ans.append(f"#{t} {res}")
for a in ans:
    print(a)