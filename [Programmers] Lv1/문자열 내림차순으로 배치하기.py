def solution(s): #문자열
    return "".join(sorted(s,reverse=True)) #내림차순 정렬 후 join으로 문자열로 반환

'''
평균 실행 시간 : 0.01 평균 메모리 사용량: 10.12
'''