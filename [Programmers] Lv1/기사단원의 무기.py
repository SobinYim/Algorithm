#sol1
def solution(number, limit, power): #기사단원 수, 공격력 제한 수치, 제한 수치를 초과한 기사가 사용할 무기의 공격력
    div=[2]*number #약수
    ans=0 #공격력의 합
    for i in range(2,int(number**.5)+1): #곱한 수를 리스트 인덱스로 접근하여 약수의 개수에 더한다
        for j in range(i,(number//i)+1):
            if i==j:
                div[i*j-1]+=1
            else:
                div[i*j-1]+=2
    for i in div: #공격력 계산
        ans+=power if i>limit else i
    return ans-1 #div 생성 시 1 역시 일괄적으로 2로 들어가서 생기는 오차 1 감하여 줌

#sol2
def solution(number, limit, power): #기사단원 수, 공격력 제한 수치, 제한 수치를 초과한 기사가 사용할 무기의 공격력
    div=[set() for _ in range(number)] #약수
    ans=0 #공격력의 합
    for i in range(1,int(number**.5)+1): #곱한 수를 리스트 인덱스로 접근하여 약수를 추가한다
        for j in range(i,(number//i)+1):
            div[i*j-1].update([i,j])
    for i in div: #공격력 계산
        ans+=power if len(i)>limit else len(i)
    return ans

#sol3
from math import ceil
def solution(number, limit, power): #기사단원 수, 공격력 제한 수치, 제한 수치를 초과한 기사가 사용할 무기의 공격력
    ans=0 #공격력의 합
    div=0 #약수의 개수
    for n in range(1,number+1):
        ans+=div
        div=0
        if n**.5%1==0: #제곱근이 정수라면 약수의 개수는 홀수
            div+=1
        for i in range(1,ceil(n**.5)): #제곱근까지의 수를 나누어 약수인지 판단한다
            if n%i==0:
                div+=2
            if div>limit: #약수가 제한 수치 이상일 때 power 사용하고 break
                div=power
                break
    return ans+div #총 공격력에 합산되지 않은 마지막 공격력 합산

'''
sol1
평균 실행 시간 : 25.31 평균 메모리 사용량: 10.41
sol2
평균 실행 시간 : 121.0 평균 메모리 사용량: 44.31
sol3
평균 실행 시간 : 337.02 평균 메모리 사용량: 10.29

sol3>sol2>sol1 순으로 짰다
이미 계산한 부분을 다시 연산해야 하는 게 마음에 안 들어서 sol2를 짰고 더 개선할 수 있을 것 같아서 sol1을 짰다
sol3에서는 모든 수에 1부터 n의 제곱근까지 순회하여 느리지만 약수의 개수만 구하여서 메모리 사용량이 적고
sol2에서는 연산이 적어 빠르지만 약수를 set에 저장해 주다 보니 메모리 사용량이 많다
sol1에서는 두 방법의 장점을 합쳐서 약수의 개수만 구하되, 두 수의 곱으로 접근하여 실행 시간도 빠르고 메모리 사용량도 적다

약수에 대한 접근 방식도 다르다
sol3에서는 작은 수부터 차례로 1~제곱근으로 n을 나눈 나머지로 약수를 판단하는 식으로 접근하였고
sol2에서는 작은 수부터 차례로 n~number//n의 곱으로 접근하여 중복 연산(Ex_6을 약수로 가지고 있다면 2, 3 역시 약수)을 피하였다
sol1은 sol2와 같다
'''