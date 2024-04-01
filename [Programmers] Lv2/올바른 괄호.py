def solution(s): #'[(',')']로만 이루어진 문자열 s
    if s.count("(")!=s.count(")"): #괄호의 짝이 안 맞으면 return False
        return False
    c=0
    for i in s:
        c=c-1 if i==")" else c+1 #괄호가 열리면 c에 +1, 닫히면 -1을 해준다
        if c<0: #c가 0 밑으로 내려가면(괄호가 열리지 않았는데 닫힘) return False
            return False
    return True #괄호 짝이 맞기 때문에 열린 채로 끝나지 않음==True

'''
[효율성 테스트] 평균 실행 시간 : 4.02 평균 메모리 사용량: 10.15
'''