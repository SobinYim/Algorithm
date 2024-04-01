from collections import Counter
def solution(participant, completion): #참가자, 완주자
    ans=Counter(participant)-Counter(completion) #차집합
    return list(ans.keys())[0] #남은 사람이 낙오자

'''
[효율성 테스트]평균 실행 시간 : 55.15 평균 메모리 사용량: 32.0

해시 함수를 이용해서는 
def solution(participant, completion):
    hash_loser=sum([hash(a) for a in participant])-sum([hash(a) for a in completion])
    for a in participant:
        if hash(a)==hash_loser:
            return a
이렇게 풀면 된다고 한다,, 진짜 정석 같은 풀이
사실 당연한 건데 익숙하지 않으니까 쓸 생각도 못 하게 되는 것 같다 반성반성
심플한데 심지어 속도도 빠름 정말 짱이다..
'''