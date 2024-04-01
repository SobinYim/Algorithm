from collections import Counter
from math import ceil
def solution(people, limit): #사람들의 몸무게, 구명보트의 무게 제한
    answer=0
    c=Counter(people)
    for i in list(filter(lambda x: x>limit-40,c.keys())): #혼자 탈 수밖에 없는 사람들
        answer+=c.pop(i)
    while c:
        mx=max(c.keys()) #남은 사람 중 가장 무거운 무게
        mn=min(c.keys()) #남은 사람 중 가장 가벼운 무게
        if limit<mx+mn: #mx와 mn이 함께 탔을 때 무게 제한을 넘길 경우
            answer+=c.pop(mx) #가장 무거운 사람만
            continue
        if mx==mn: #mx와 mn이 같을 경우==중간값
            if mx>limit/2:
                answer+=c.pop(mx)
            else:
                answer+=ceil(c.pop(mx)/2)
            break
        if c[mx]>c[mn]: #몸무게가 mx인 사람 수가 mn인 사람 수보다 많으면
            c[mx]-=c[mn]
            answer+=c.pop(mn)
        elif c[mx]==c[mn]: #몸무게가 mx인 사람 수와 mn인 사람 수가 같으면
            answer+=c.pop(mn)
            c.pop(mx)
        else: #몸무게가 mn인 사람 수가 mx인 사람 수보다 많으면
            c[mn]-=c[mx]
            answer+=c.pop(mx)
    return answer

'''
[효율성 테스트] 평균 실행 시간 : 1.9 평균 메모리 사용량: 10.36

길지만.... 빠르다는 것에 의의를 두고...
경우의 수를,,, if문으로 처리했다
Counter라 중복 값을 처리하기도 하고 또 기본적으로 딕셔너리라 deque나 index를 이용하는 다른 풀이들에 비해 유의미하게 빨랐던 것 같다

아래는 index로 접근하는 풀이법! 심플하고 다른 풀이에 비해서 성능도 잘 나와서 마음에 든다
def solution(people, limit) :
    answer = 0
    people.sort()
    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer
[효율성 테스트] 평균 실행 시간 : 7.67 평균 메모리 사용량: 10.5
'''