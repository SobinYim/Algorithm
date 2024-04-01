#sol1
def solution(n, works): #퇴근까지 남은 시간, 남은 일의 작업량
    if sum(works)-n<=0: #퇴근까지 모든 일을 마칠 수 있다면 return 0
        return 0
    works=sorted(works,reverse=True)
    l=len(works)
    while n:
        mx=works[0] #가장 오래 걸리는 작업
        mx_cnt=works.count(mx) #mx와 동일한 시간이 걸리는 작업 수
        diff=mx-works[mx_cnt] if mx_cnt!=l else mx_cnt-1 #가장 오래 걸리는 작업과 다음으로 오래 걸리는 작업의 소요 시간 차, 모든 작업에 동일한 시간이 걸린다면 길이-1
        if mx_cnt*diff<=n: #가장 오래 걸리는 작업들을 다음으로 오래 걸리는 작업 시간까지 처리하는 데 걸리는 시간이 n 이하라면
            works[:mx_cnt]=[mx-diff]*mx_cnt
            n-=diff*mx_cnt
        else: #다음 작업까지 처리하는 데 걸리는 시간이 n보다 크다면
            tmp=n//mx_cnt
            works[:mx_cnt]=[mx-tmp]*mx_cnt
            n%=mx_cnt
            works[:n]=[works[0]-1]*(n) #앞에서부터 1시간씩 처리
            break
    return sum([i**2 for i in works]) #야근 피로도

#sol2
def solution(n, works): #퇴근까지 남은 시간, 남은 일의 작업량
    if sum(works)-n<0: #퇴근까지 모든 일을 마칠 수 있다면 return 0
        return 0
    works=sorted(works,reverse=True)
    while n:
        tmp=min(works.count(works[0]),n) #가장 오래 걸리는 작업 수와 n 중 작은 것
        for i in range(tmp):
            works[i]-=1
        n-=tmp
    return sum([i**2 for i in works]) #야근 피로도

'''
#sol1
[효율성 테스트] 평균 실행 시간 : 11.29 평균 메모리 사용량: 10.25
#sol2
[효율성 테스트] 평균 실행 시간 : 197.72 평균 메모리 사용량: 10.2

sol1>sol2 순으로 짰다
야근 피로도를 최소화하기 위해서는 최댓값을 깎아야 한다
sol1에서는 최댓값들을 다음으로 큰 값까지 깎는 것을 반복하고
sol2에서는 최댓값을 for문을 이용해 -1씩 깎는 것을 반복한다
sol1은 확실히 빠르지만 리스트의 구간에 할당을 해서 길이가 같아서 문제없을 걸 알면서도 조금 불안했다,,
for문을 이용해서 대체를 해도 되겠다.. 그런데 굳이?라는 생각도 들고

from heapq import heapify, heappush, heappop
def solution(n, works):
    heapify(works := [-i for i in works])
    for i in range(min(n, abs(sum(works)))):
        heappush(works, heappop(works)+1)
    return sum([i*i for i in works])
[효율성 테스트] 평균 실행 시간 : 304.45 평균 메모리 사용량: 10.2
다른 사람의 풀이에서 본 힙을 이용한 풀이! 코드가 심플해서 좋다!
힙도 좀 써 봐야 하는데 막상 문제 풀 때 생각이 안 난다
'''