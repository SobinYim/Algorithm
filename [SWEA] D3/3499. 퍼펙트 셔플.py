T=int(input()) #tc 개수
for t in range(1,T+1):
    n=int(input()) #카드 수
    card=list(map(str,input().split())) #카드가 놓인 순서
    s=n//2
    d1=card[:-s] #앞쪽 카드
    d2=card[-s:] #뒤쪽 카드
    res=" ".join(map(lambda x: d1[x]+" "+d2[x],range(len(d2)))) #차례로 d1, d2에서 한 장씩 꺼내옴
    if len(card)%2==1: #카드가 홀수면 마지막 카드를 뒤에 붙여줌
        res+=f" {d1[-1]}"
    print(f"#{t}",res)