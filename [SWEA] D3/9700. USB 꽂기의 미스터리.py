T=int(input()) #tc 개수
for t in range(1,T+1):
    p,q=map(float,input().split()) #처음 USB를 꽂을 때 올바른 면으로 USB를 꽂았을 확률 p, 올바르게 꽂았을 때 정상적으로 USB가 꽂힐 확률 q
    s1=(1-p)*q #USB를 1번 뒤집었을 때 USB가 꽂힐 확률
    s2=p*(1-q)*q #USB를 2번 뒤집었을 때 USB가 꽂힐 확률
    res="YES" if s1<s2 else "NO"
    print(f"#{t}",res)