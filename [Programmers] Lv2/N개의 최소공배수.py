#sol
from math import gcd
def solution(arr): #자연수 배열
    n=arr.pop() #처음 요소 할당
    for i in arr:
        n*=i//gcd(i,n) #n과 i의 최소공배수
    return n

#sol1
max_n=101
p=[0]*max_n
p[:2]=1,1
for i in range(max_n): #에라토스테네스의 체
    if p[i]:
        continue
    else:
        for j in range(i*i,max_n,i):
            p[j]=1
prime_number=[idx for idx,i in enumerate(p) if not i]
def solution(arr): #자연수 배열
    arr.sort(reverse=True)
    n=arr.pop(0) #처음 요소 할당
    for i in arr:
        if not n%i: #n이 이미 i의 배수라면 continue
            continue
        elif i in prime_number: #i가 소수라면 n에 바로 곱한다
            n*=i
        else: #그 외의 경우 i와 n이 모두 나누어떨어지는 수 탐색
            for j in range(i-1,0,-1):
                if n%j==i%j==0:
                    n*=i//j #n과 i의 최소공배수
                    break
    return n

#sol2
from collections import Counter
from functools import reduce
max_n=101
p=[0]*max_n
p[:2]=1,1
for i in range(max_n): #에라토스테네스의 체
    if p[i]:
        continue
    else:
        for j in range(i*i,max_n,i):
            p[j]=1
prime_number=[idx for idx,i in enumerate(p) if not i]
def prime_factorization(n): #정수 n이 주어지면 이를 소인수분해 하여 Counter형식으로 반환
    if n==1 or n in prime_number: #n이 1 혹은 소수일 때
        return Counter([n])
    factor=[]
    idx=0
    div=prime_number[idx]
    while True: #소인수분해
        if n%div:
            idx+=1
            div=prime_number[idx]
        else:
            n//=div
            factor.append(div)
            if n==1:
                break
    return Counter(factor)
def solution(arr): #자연수 배열
    union_pf=reduce(lambda x,y:x|y,map(prime_factorization,arr)).elements() #arr의 각 요소들을 소인수분해 한 결과의 합집합
    return reduce(lambda a,b:a*b,union_pf) #각 요소들을 곱하여 최소 공배수 계산

#sol3
from functools import reduce
def solution(arr):
    max_n=101
    p=[0]*max_n
    p[:2]=1,1
    for i in range(max_n): #에라토스테네스의 체
        if p[i]:
            continue
        else:
            for j in range(i*i,max_n,i):
                p[j]=1
    prime_number=[idx for idx, i in enumerate(p) if not i]
    factor=dict() #소인수
    for n in arr:
        idx=0 #소수 리스트 인덱스
        cnt=0 #지수
        while True:
            div=prime_number[idx] #소인수인지 검사할 소수
            if n%div==0:
                n//=div
                cnt+=1
            else:
                if cnt>0: #해당 소인수로 1번 이상 나누었다면 사전 갱신
                    if div not in factor.keys():
                        factor[div]=cnt
                    else:
                        factor[div]=max(factor[div],cnt)
                cnt=0
                idx+=1
                if n==1:
                    break
    answer = reduce(lambda a,b:a*b,[i**j for i,j in factor.items()]) #최소공배수 계산
    return answer


'''
#sol
평균 실행 시간 : 0.0 평균 메모리 사용량: 10.16
#sol1
평균 실행 시간 : 0.01 평균 메모리 사용량: 10.12
#sol2
평균 실행 시간 : 0.072 평균 메모리 사용량: 10.29
#sol3
평균 실행 시간 : 0.035 평균 메모리 사용량: 10.28

sol3>sol2>sol1>sol 순으로 짰다

sol과 sol1은 토대가 같다 arr를 순회하며 i에 n과 i의 최대공약수를 나눈 몫을 최소공배수 n에 곱하며 새로운 최소공배수를 만들어준다
sol은 '쉽고 짧게' 짰고 math.gcd() 사용으로 시간을 대폭 단축했다
sol1은 j를 i부터 감소시키며 최대공약수를 구했다 n%i가 0이라면 그냥 넘기고 소수 list를 같이 써서 소수라면 바로 n에 곱했다
매번 소수를 모두 검사하는 게 비효율적일 것 같아서 작성해 봤다
그리고 정렬하여 큰 것부터 검사하는 게 순회를 덜 한다 물론 정렬하는 것까지 계산에 넣으면 뭐가 더 효율적일지까지는 모르겠다..

sol2와 sol3도 같은 내용이다 arr를 순회하며 소인수분해하고 이 합집합을 곱하여서 최소공배수를 구한다
차이점은 sol2는 Counter로 소인수를 담고, 소인수분해 과정을 함수로 분리했다
sol3은 소인수를 key로, 지수를 value로 갖는 dictionary로 담고, 소인수분해 과정을 함수로 분리하지 않고 한 번에 처리했다
sol2는 list>Counter>union.element()>list 등,,, 형 변환이 자주 이루어져서 더 오래 걸리지 않았나 싶다 
'''