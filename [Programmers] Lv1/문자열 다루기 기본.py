def solution(s):
    answer=len(s) in [4,6] and s.isdigit() #s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인
    return answer

'''
평균 실행 시간 : 0.004 평균 메모리 사용량: 10.177
'''