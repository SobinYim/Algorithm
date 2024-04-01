#sol1
from math import ceil
def solution(n, stations, w): #아파트 수, 기지국 위치, 전파 도달 거리
    n+=1
    ans,prev=0,1
    width=2*w+1
    for i in stations:
        signal=i-w #신호가 시작하는 범위
        if prev<signal: #이전 기지국의 끝 범위보다 작다면
            ans+=ceil((signal-prev)/width) #남는 범위를 전파 도달 거리로 나눈 것을 올림한 값을 ans에 합함
        prev=i+w+1 #끝 범위
    if prev<n: #끝 부분
        ans+=ceil((n-prev)/width)
    return ans

#sol2(시간 초과)
def solution(n, stations, w):
    ans=0
    signals=set(range(n))
    for i in stations:
        signals-=set(range(i-w-1,i+w)) #신호가 닿는 범위를 차집합
    while signals:
        ans+=1
        tg=min(signals)
        signals-=set(range(tg,tg+1+w*2)) #가장 작은 값을 시작점으로 하는 기지국 설치
    return ans

'''
#sol1
[효율성 테스트] 평균 실행 시간 : 1.6 평균 메모리 사용량: 10.45
#sol2
평균 실행 시간 : 0.02 평균 메모리 사용량: 10.23

sol2>sol1로 짰다
sol2 비슷하게 뭐 리스트로도 짜고 해봤는데 죄다 효율성 타임아웃이라 sol1를 짰다
어떻게 수학적으로 접근할 만한 부분이 없나 고민을 좀 했다,,
일단 순회를 한 번만 돌리고 범위로 접근해서 다른 배열 등을 안 써서 시간을 많이 줄일 수 있었다
if 부분은 없어도 결과엔 영향을 안 미치지만 있는 쪽이 시간 절약이 된다

def solution(n, arr, w):
    bef=-w
    cnt=0
    ww=w*2+1
    for x in arr:
        cnt+=(x-bef-1)//ww
        bef=x
    return cnt+(n+w-bef)//ww
[효율성 테스트] 평균 실행 시간 : 0.94 평균 메모리 사용량: 10.45
다른 사람의 풀이에서 본 풀이!
나는 ceil 계산을 해줘야 하는데 이 풀이에서는 그럴 필요도 없고 로직 자체도 심플해서 아주 굿이다
'''