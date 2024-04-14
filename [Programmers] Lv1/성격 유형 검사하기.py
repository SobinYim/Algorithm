def solution(survey, choices): #질문마다 판단하는 지표, 검사자가 선택한 선택지
    kfti=dict((i,0) for i in ["RT","CF","JM","AN"]) #지표:점수 딕셔너리
    for s,c in zip(survey,choices):
        if s not in kfti.keys(): #지표가 딕셔너리 안에 없다면 뒤집고 -점수를 더한다
            kfti[s[::-1]]-=c-4
        else:
            kfti[s]+=c-4
    ans="".join([k[v>0] for k,v in kfti.items()]) #지표의 점수가 0 이하라면(False) 앞 유형, 1 이상이라면 뒤 유형
    return ans

'''
평균 실행 시간 : 0.12 평균 메모리 사용량: 10.14

무난했던 문제!
"RT"와 "TR"을 어떻게 할까 고민하다가 뒤집어서 점수를 빼주기로 했다
따로 넣고 나중에 합쳐도 되겠으나 이게 가장 간단하다고 생각했다

지표['RT'] = 지표['TR'] = {'R': 0, 'T': 0,}
다른 사람의 풀이에서 본 부분인데 이런 방법이 있구나 싶었다
같은 객체를 가져오니까,, 어느 쪽이 들어가더라도 값이 같이 오른다!

다른 사람의 풀이
from collections import defaultdict
def solution(survey, choices):
    indicator = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    answer = ''
    personality = defaultdict(int)
    for s, c in zip(survey, choices):
        if c < 4:
            personality[s[0]] += (4 - c)
        elif c > 4:
            personality[s[1]] += (c - 4)
    for i in indicator:
        if personality[i[0]] >= personality[i[1]]:
            answer += i[0]
        else:
            answer += i[1]
    return answer
평균 실행 시간 : 0.08 평균 메모리 사용량: 10.27
아주 정석 풀이 같다!
각 유형 마다 점수를 계산하고 높은 쪽의 점수 유형을 낸다
직관적인 데다 빠르기까지 하다,,, 아주 마음에 든다 굿!
'''