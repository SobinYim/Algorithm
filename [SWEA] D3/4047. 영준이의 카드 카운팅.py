T=int(input()) #tc 개수
s=["S","D","H","C"]  # 카드의 무늬
for t in range(1,T+1):
    c=input() #카드
    li=[set(),set(),set(),set()] #무늬별 카드
    res=0
    for i in range(0,len(s),3): #무늬와 값 TXY 꼴이므로 셋씩 끊음
        tgs,tgv=s.index(c[i]),c[i+1:i+3] #해당 카드의 무늬와 값
        if (len(c)>156) or (li[tgs].issuperset([tgv])): #카드의 길이가 156 이상이거나 해당 카드가 이미 카드셋에 있으면 중복 카드가 있다는 의미이므로
            res=-1
            break
        li[tgs].add(tgv) #카드를 카드셋에 추가
    res=["ERROR"] if res==-1 else map(lambda x: 13-len(x),li)
    print(f"#{t}",*res)