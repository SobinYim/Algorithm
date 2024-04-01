def solution(k, score): #명예의 전당 목록 길이, 일자별 가수들의 점수
    h,a=[],[] #명예의 전당, 발표 점수
    for i in score:
        if len(h)<k: #명예의 전당에 빈 자리가 있을 때
            h+=[i]
        elif min(h)<i:
            h.remove(min(h))
            h+=[i]
        a+=[min(h)]
    return a

'''
평균 실행 시간 : 0.96 평균 메모리 사용량: 10.25
'''