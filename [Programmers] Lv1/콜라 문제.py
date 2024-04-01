from math import ceil
def solution(a, b, n): #빈 병 a개를 b개로 교환, 현재 가지고 있는 병
    return ceil((n-a+1)/(a-b))*b

'''
평균 실행 시간 : 0.003 평균 메모리 사용량: 10.114

규칙 찾아서 풀었다,,
(n - b) // (a - b) * b
보고 살짝 울 뻔했다,,, 틀은 같지만 훨씬 깔끔하고 예쁘다,,
그래도 재밌었던 문제
'''