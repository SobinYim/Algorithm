from collections import deque
from math import ceil
def solution(scoville, K): #모든 음식의 스코빌 지수, 목표 스코빌 지수
    ans=0
    less_spicy=deque(sorted(filter(lambda x:x<K,scoville))) #덜 매운 음식(이미 K 이상인 음식 리스트에서 제외)
    mixed=deque() #섞은 음식
    flag=len(scoville)!=len(less_spicy) #이미 K 이상인 음식이 있다면 ans는 -1가 아님
    while len(less_spicy)+len(mixed)>1: #남은 음식이 2개 이상이면 루프
        tmp=[] #섞을 음식
        for _ in range(2):
            if not less_spicy:
                tmp.append(mixed.popleft())
            elif not mixed:
                tmp.append(less_spicy.popleft())
            elif less_spicy[0]<=mixed[0]:
                tmp.append(less_spicy.popleft())
            else:
                tmp.append(mixed.popleft())
        new_scoville=tmp[0]+tmp[1]*2
        if new_scoville<K: #새로운 음식의 스코빌 지수가 K보다 작다면
            mixed.append(new_scoville)
        else: #K보다 크다면(==이후 섞은 음식의 스코빌 지수는 반드시 K 이상)
            flag=True
            ans+=ceil((len(mixed)+len(less_spicy))/2)+1
            break
        ans+=1
    else:
        if any([mixed,less_spicy]): #mixed, less_spicy가 존재하면 ans+1
            ans+=1
    return ans if flag else -1

'''
[효율성 테스트] 평균 실행 시간 : 505.58 평균 메모리 사용량: 38.48

힙 문제지만 deque를 사용해서 풀었다
속도는 잘 나오는데,, while문 조건에서 mixed와 less_spicy의 길이를 계속 가져오는 거랑 filter 부분이 조금 마음에 안 든다
뭔가 이렇다 할 방법이 생각 안 나서 일단 넘어가기로

힙을 사용한 풀이:
import heapq as hq
def solution(scoville, K):
    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  
    return answer
[효율성 테스트] 평균 실행 시간 : 846.38 평균 메모리 사용량: 30.9
힙을 사용하면 코드가 많이 간결해진다!
평균 실행 시간은 조금 느리지만 메모리 사용량이 적고 일단 뇌가 편하다,, 굿!
'''