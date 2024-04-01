T=int(input()) #tc 개수
for t in range(1,T+1):
    n,m,k=map(int,input().split()) #n=손님 수, m=붕어빵을 굽는 시간, k=1회 당 붕어빵 생산 개수
    li=list(map(int,input().split())) #손님이 도착하는 시간
    s=sorted(set(li))
    cb,c=0,0 #손님, 붕어빵 수
    res="Possible"
    for i in s: #중복 제거 후, 정렬한 리스트
        cb+=li.count(i) #손님
        c=(i//m)*k #붕어빵 = (현재 초//붕어빵을 구울 때 걸리는 시간)*한 번에 구울 수 있는 붕어빵 개수
        if c<cb:
            res="Impossible"
            break
    print(f"#{t}",res)