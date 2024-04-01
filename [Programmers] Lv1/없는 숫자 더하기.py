#sol1
def solution(numbers): #정수 배열
    return sum(filter(lambda _: _ not in numbers, range(10))) #0-9중 number에 없는 수를 filter로 걸러내서 합계
#sol2
def solution(numbers): #정수 배열
    return sum([i for i in range(10) if i not in numbers]) #0-9중 number에 없는 수를 for문으로 걸러내서 합계
#sol3
def solution(numbers): #정수 배열
    return sum(set(range(10)).difference(numbers)) #차집합 후 합계

'''
#1
평균 실행 시간 : 0.008 평균 메모리 사용량: 10.156
#2
평균 실행 시간 : 0.003 평균 메모리 사용량: 10.122
#3
평균 실행 시간 : 0.009 평균 메모리 사용량: 10.133

여러 가지 방법을 시도해 봤는데 예상 가능한 결과,,
'''