#sol
from math import gcd
from functools import reduce
def is_coprime(array, div): #array의 모든 요소가 div로 나누어지지 않는지 판단
    for i in array:
        if not i % div:
            return False
    else:
        return True
def solution(arrayA, arrayB): #철수의 카드, 영희의 카드
    flag = False
    divA = reduce(gcd, arrayA) #arrayA의 최대공약수
    divB = reduce(gcd, arrayB) #arrayB의 최대공약수
    if divA!=1: #divA가 1이 아니라면 arrayB와 서로소 판단
        flag = is_coprime(arrayB, divA)
    if divB!=1: #divB가 1이 아니라면 arrayB와 서로소 판단
        if is_coprime(arrayA, divB):
            return max(divA, divB) if flag else divB #둘 다 조건을 만족한다면 큰 값을, divB만 만족한다면 divB를 반환
    return divA if flag else 0 #divA만 조건을 만족한다면 divA를, 둘 다 조건을 만족하지 않는다면 0을 반환

#sol1
from math import gcd
from functools import reduce
def is_coprime(array, div): #array의 모든 요소가 div로 나누어지지 않는지 판단
    for i in array:
        if not i % div:
            return False
    else:
        return True
def solution(arrayA, arrayB): #철수의 카드, 영희의 카드
    divA = reduce(gcd, arrayA) #arrayA의 최대공약수
    divB = reduce(gcd, arrayB) #arrayB의 최대공약수
    flag = is_coprime(arrayB, divA)
    if is_coprime(arrayA, divB):
        return max(divA, divB) if flag else divB  #둘 다 조건을 만족한다면 큰 값을, divB만 만족한다면 divB를 반환
    else:
        return divA if flag else 0 #divA만 조건을 만족한다면 divA를, 둘 다 조건을 만족하지 않는다면 0을 반환

'''
sol
평균 실행 시간 : 16.19 평균 메모리 사용량: 19.91
sol1
평균 실행 시간 : 16.01 평균 메모리 사용량: 19.87

sol과 sol1은 같은 풀이다
sol1이 sol에서 조건을 없애서 코드 길이를 더 짧게 한 버전인데
오차인가 싶기는 하지만 몇 번 돌려봐도 요상하게 sol1이 시간이 더 적게 걸린다
for문을 돌리는 것도 아니고 조건문 하나인데 알 수 없는 일이다,,,
추측하건대,,, 케이스를 여러 번 반복한 건가 싶다...?
'''