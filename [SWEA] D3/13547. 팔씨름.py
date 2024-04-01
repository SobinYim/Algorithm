T=int(input()) #tc 개수
for t in range(1,T+1):
    s=input() #진행한 경기 결과
    c=s.count("o")-len(s) #소정이의 승리 횟수-진행한 경기 수
    res="YES" if c>-8 else "NO" #c가 -8보다 작다면 소정이가 이길 수 있는 방법이 없으므로 "NO"
    print(f"#{t}",res)