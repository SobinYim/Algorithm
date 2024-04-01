#sol1
from collections import deque
def solution(s): #괄호 문자열
    if len(s)%2: #괄호 문자열의 길이가 홀수라면 return 0
        return 0
    ans=0
    brackets={")":"(","]":"[","}":"{"} #닫는 괄호:여는 괄호 딕셔너리
    s=deque(s)
    def fn_valid(s): #올바른 괄호 문자열인지 검사
        stack=[]
        for i in s:
            if stack and i in brackets.keys(): #stack이 존재하고 i가 닫는 문자열이면
                if stack.pop()!=brackets[i]: #i와 stack[-1]이 괄호 쌍이 아니라면
                    return False
            else:
                stack.append(i)
        return not stack
    for _ in range(len(s)):
        s.rotate(1) #회전
        if s[0] not in brackets.keys(): #첫 번째 요소가 여는 괄호라면 올바른 괄호 문자열인지 검사
            ans+=fn_valid(s)
    return ans

#sol2
def solution(s): #괄호 문자열
    ans,rot=0,0 #올바른 괄호 문자열의 수, 괄호 문자열 회전
    l=len(s)
    brackets=["()","[]","{}"] #괄호
    if l%2 or sum(map(lambda x: s.count(x[0])!=s.count(x[1]),brackets)): #괄호 문자열의 길이가 홀수이거나 여는 괄호와 닫는 괄호의 수가 맞지 않으면 return 0
        return 0
    while rot<l: #회전 수가 괄호 문자열의 길이보다 작을 때 루프
        stack=[]
        for i in s:
            if stack and stack[-1]+i in brackets: #stack이 존재하고 stack의 마지막 요소+i가 올바른 괄호 쌍이라면
                stack.pop()
            else:
                stack.append(i)
        ans+=not stack
        if ans: #ans가 존재한다면 2만큼 회전
            rot+=2
            s=s[2:]+s[:2]
        else:
            rot+=1
            s=s[1:]+s[0]
    return ans

'''
#sol1
평균 실행 시간 : 23.27 평균 메모리 사용량: 10.31
#sol2
평균 실행 시간 : 70.92 평균 메모리 사용량: 10.23

sol2>sol1로 짰다
처음에는 함수로 분리하지 않고 while을 이용하여, 괄호 문자열을 deque가 아니라 list로, 괄호 쌍을 딕셔너리가 아니라 리스트 형태로 짰는데
리스트 형태로 짜니까 조건 거는 게 너무 한정적이어서(걸려면 걸 수도 있겠지만 코드가 너무 더러워지니까,,) 딕셔너리로 하여 다시 짰다
'''