#sol1
T=int(input()) #tc 개수
for t in range(1,T+1):
    n=int(input()) #즐거운 날의 수
    d=set() #즐거운 날의 목록
    for i in range(n):
        d.add(int(input()))
    d.discard(1) #모든 배가 들어오는 날이므로 사용하지 않음
    res=0
    while d: #d가 비어있지 않다면 차집합을 반복
        for i in d:
            res+=1
            d.difference_update(range(i,max(d)+1,i-1))
            break
    print(f"#{t}",res)

#sol2
T=int(input()) #tc 개수
for t in range(1,T+1):
    n=int(input()) #즐거운 날의 수
    d=[] #즐거운 날의 목록
    for i in range(n):
        d.append(int(input()))
    res=0
    d.pop(0) #첫째날은 모든 배가 들어오는 날이므로 사용하지 않음
    s=set() #배가 방문한 날짜
    for i in d:
        if i not in s:
            s=s|set(range(i,max(d)+1,i-1))
            res+=1
    print(f"#{t}",res)

'''
처음에는 즐거운 날의 목록을 list로 받고, set 변환하여 차집합을 해주는 방식(sol0)으로 짰는데
형 변환을 반복하는 게 비효율적으로 느껴져서 아예 set로 받도록 짰다
그랬더니 맨 앞에서 요소 한 개씩 꺼내오는 게 문제라 어떻게 억지로 풀었는데 생각보다 시간 감축도 안되고 상당히 마음에 안들어서 생각해 본 sol2
에라토스테네스의 체에서 착안, 모든 날짜에 배가 도착하는 게 아니다보니 리스트의 요소를 바꾸는 것보다는 set를 이용하는 방법을 택했다

sol0(1,433ms) => sol1(622ms) => sol2(513ms)
'''