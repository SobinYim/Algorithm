def solution(s): #문자열
    s=s.lower() #소문자로 통일
    answer=s.count("p")==s.count("y")
    return answer

'''
평균 실행 시간 : 0.0 평균 메모리 사용량: 10.15
'''