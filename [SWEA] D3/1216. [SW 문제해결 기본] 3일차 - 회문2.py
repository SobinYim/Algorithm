#sol1 : 재귀
def fn_p(x,n=100): #문자열x에서 길이가 n(최대 길이인 100부터 감소)인 회문을 탐색, 회문이 있으면 n을 반환하고 회문이 없다면 n-1으로 재귀
    k=101-n
    for i in range(k):
        if x[i:i+n]==x[i:i+n][::-1]:
            return n
    return fn_p(x,n-1)

for _ in range(10):
    li=[] #글자판 초기화
    t=int(input()) #tc
    for i in range(100):
        li.append(input())
    li.extend(list(map(list, zip(*li)))) #전치행렬 리스트에 추가
    res=max(map(fn_p,li)) #글자판의 회문 길이가 가장 긴 것을 res에 저장
    print(f"#{t}",res)

#sol2
def fn_p(x,n): #문자열x에서 길이가 n인 회문을 탐색, 회문이 있으면 1을 아니라면 0을 반환
    k=101-n
    for i in range(k):
        if x[i:i+n]==x[i:i+n][::-1]:
            return 1
    return 0
for _ in range(10):
    li=[] #글자판 초기화
    t=int(input()) #tc
    for i in range(100):
        li.append(input())
    li.extend(list(map(list, zip(*li)))) #전치행렬 리스트에 추가
    s,res=0,101 #s가 0이면 회문이 없다는 의미이므로 반복 실행, res=현재 탐색중인 회문의 길이
    while not s:
        res-=1
        s=sum(map(lambda x: fn_p(x,res),li)) #하나라도 1이 나오면 반복을 멈추고 현재 res 값을 출력
    print(f"#{t}",res)

'''
재귀는 문자열 하나씩 탐색하기 때문에 가장 큰 n이 나와도 바로 멈추지 않음
sol2에서는 while문을 이용하여 회문 길이 n이 최대가 되면 바로 멈출 수 있게 하였음 
드라마틱한 결과는 아니나 tc 평균 3.3s => 2.9s로 감소
'''