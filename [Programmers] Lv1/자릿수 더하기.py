#sol1
def solution(n): #자연수
    return n if n < 10 else solution(n//10)+n%10 #n이 10 미만이라면 멈추고 아니라면 끝 자릿수를 더하고 n//10으로 재귀

#sol2
def solution(n): #자연수
    answer=0
    while n: #각 자리수 합
        answer+=n%10
        n//=10
    return answer

#sol3
def solution(n): #자연수
    answer=sum(map(int,str(n))) #문자형 변환을 통해 iterable하게 바꿔주고 이를 다시 int형 변환한 것의 합
    return answer

'''
#sol1
평균 실행 시간 : 0.0 평균 메모리 사용량: 10.19
#sol2
평균 실행 시간 : 0.0 평균 메모리 사용량: 10.16
#sol3
평균 실행 시간 : 0.02 평균 메모리 사용량: 10.33

같은 결의 문제가 계속 나온다..
이번 문제는 재귀로도 풀어봤는데 심플하고 빠르고 좋았다
'''