from math import isqrt
def solution(n): #정수
    answer=0
    for i in range(1,isqrt(n)+1): #약수 구하기
        if n%i==0:
            answer+=sum({i,n//i}) #set()를 이용해서 n이 제곱수인 경우 처리
    return answer

'''
평균 실행 시간 : 0.01 평균 메모리 사용량: 10.11

**.5 대신에 isqrt를 사용해 보았다
import 시간이 있기도 하고 연산 속도가 둘이 차이가 거의 나지 않을 거라고 생각했는데 isqrt가 빠른 것으로 나와서 좀 의외였다
물론 .01ms의 근소한 차이라 오차 범위일 수도 있긴 하다,,
테케 평균 실행 속도가 기본적으로 빠르게 나올 수밖에 없는 경우에 기분은 좋긴 하지만 어느 부분에서 성능 차이가 유의미하게 나는지 알기는 어려워져서 조금 아쉽다
'''