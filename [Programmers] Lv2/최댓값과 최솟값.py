def solution(s): #문자열
    num=list(map(int,s.split())) #공백을 기준으로 나눠주고 int형 변환
    answer=f"{min(num)} {max(num)}"
    return answer

'''
평균 실행 시간 : 0.03 평균 메모리 사용량: 10.28
'''