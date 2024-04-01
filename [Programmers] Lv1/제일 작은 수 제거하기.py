def solution(arr): #정수 배열
    arr.remove(min(arr)) #최솟값 제거
    return arr if arr else [-1]

'''
평균 실행 시간 : 0.08 평균 메모리 사용량: 10.54
'''