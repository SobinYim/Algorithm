def solution(t, p): #숫자로 이루어진 문자열, 기준 문자열
    n=int(p) #대소 비교를 위해 형 변환
    s=sum(int(t[i:i + len(p)]) <= n for i in range(len(t) - len(p) + 1)) #부분 문자열 생성 후 형 변환, 대소 비교한 boolean 값의 합
    return s

'''
평균 실행 시간 : 0.77 평균 메모리 사용량: 10.27
'''