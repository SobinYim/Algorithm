#sol1
from math import factorial
def solution(n, k): #사람의 수, k번째 방법
    answer = []
    line = list(range(1, n + 1)) #줄 서는 사람
    k -= 1
    for i in range(n - 1, -1, -1):
        f = factorial(i)
        answer.append(line.pop(k // f))
        k %= f
    return answer

#sol2
from math import factorial
def solution(n, k): #사람의 수, k번째 방법
    answer = []
    line = list(range(1, n + 1)) #줄 서는 사람
    k -= 1
    for i in range(n - 1, -1, -1):
        quot, k = divmod(k, factorial(i))
        answer.append(line.pop(quot))
    return answer

#sol3
def solution(n, k): #사람의 수, k번째 방법
    answer = []
    k -= 1
    line = list(range(1, n + 1)) #줄 서는 사람
    prev = 1
    fac = [1] + [(prev := prev * i) for i in line] #1!~n! 리스트
    for i in range(n - 1, -1, -1):
        quot, k = divmod(k, fac[i])
        answer.append(line.pop(quot))
    return answer


'''
sol1
[효율성 테스트] 평균 실행 시간 : 0.012 평균 메모리 사용량: 10.16
sol2
[효율성 테스트] 평균 실행 시간 : 0.014 평균 메모리 사용량: 10.18
sol3
[효율성 테스트] 평균 실행 시간 : 0.01 평균 메모리 사용량: 10.12

수학 쪽은 오랜만인데 재밌었다
sol1은 divmod 없이 factorial 사용
sol2는 divmod와 factorial 사용
sol3은 factorial을 만들어 놓고 divmod를 사용했다
'''