def solution(s): #문자열
    tmp=[0] #인덱스 에러 방지를 위해 0 넣어놓기
    for i in s:
        if i==tmp[-1]: #tmp의 마지막 요소가 현재 i와 같을(==연달아 나왔을 경우) 경우 tmp.pop(-1)으로 제거
            tmp.pop(-1)
        else:
            tmp.append(i)
    tmp.pop(0) #처음에 넣어놨던 0 제거
    return int(not tmp) #tmp가 비어있다면 1, 아니라면 0

'''
평균 실행 시간 : 83.61 평균 메모리 사용량: 12.99
'''