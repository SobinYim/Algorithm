#sol1
def solution(user_id, banned_id): #응모자 id, 불량 사용자
    def search_combos(combos=[],step=0): #제재 아이디 경우의 수
        nonlocal matched_user,ans,l
        if step<len(matched_user):
            user=matched_user[step] #한 불량 사용자 패턴과 일치하는 응모자 id
            for i in user:
                if i not in combos: #이미 선택된 id가 아니라면
                    search_combos(combos+[i],step+1)
        else:
            combos=sorted(combos)
            if combos not in ans:
                ans.append(combos)
    matched_user=[] #불량 사용자 패턴과 일치하는 응모자 id
    for ban in banned_id:
        matched=[] #한 불량 사용자 패턴과 일치하는 응모자 id
        for uid in user_id:
            if len(ban)==len(uid): #패턴과 id의 길이가 일치하면
                for b,u in zip(ban,uid):
                    if b not in [u,"*"]: #패턴의 부분 b가 id와 일치하지 않고 마스킹된 부분이 아니라면
                        break
                else:
                    matched.append(uid)
        matched_user.append(matched)
    ans=[]
    l=len(banned_id) #불량 사용자 길이
    search_combos()
    return len(ans)

#sol2
import re
from itertools import product
def solution(user_id, banned_id): #응모자 id, 불량 사용자
    matched_user=[] #불량 사용자 패턴과 일치하는 응모자 id
    for i in banned_id:
        matched=[] #한 불량 사용자 패턴과 일치하는 응모자 id
        b=i.replace("*",".")
        for u in user_id:
            if re.fullmatch(b,u): #응모자 id가 패턴과 일치한다면
                matched.append(u)
        matched_user.append(matched)
    banned_user=set() #제재 아이디
    l=len(banned_id) #불량 사용자 길이
    for p in product(*matched_user): #경우의 수
        if len(set(p))==l:
            banned_user.add(tuple(sorted(p)))
    return len(banned_user)


'''
sol1
평균 실행 시간 : 7.99 평균 메모리 사용량: 10.24
sol2
평균 실행 시간 : 514.25 평균 메모리 사용량: 10.22

sol2>sol1 순으로 풀었다
sol1은 모듈 없이 구현한 풀이고 sol2는 re랑 product를 사용하여 풀었다
sol2는 product 생성 후, 중복을 제거하는 거라 몹시 비효율적인 풀이기는 하다,,
수학으로 풀고 싶었는데 쉽지가 않았다,,,
크게 보면 조합이 맞는데 불량 사용자 패턴마다 선택을 하면 순서가 생겨버리는 문제가 발생하는 것이다,,,(전 선택이 이후 선택에 영향을 미치니까,,,)
불가능한 경우의 수를 빼주는 방법도 생각해 봤는데 여러 패턴에 겹치는 id나,,
패턴 하나에 일치하는 id가 하나면 그 id를 다른 곳에서 못 쓰는 부분이나(카운트는 여러 곳에서 될 텐데도)
그런 여러 경우의 수를 따지다 보니 지금 당장 풀기엔 무리가 있겠다는 생각이 들었다,,, 일단 멈추고 다음을 기약하기로!

c=Counter(matched_user)
ans=set([frozenset(i) for i in (lambda x,y: combinations(x,y))(*c.popitem())])
for k,v in c.items():
    comb = combinations(k,v)
    res = set()
    for i in comb:
        for item in ans:
            if (tmp:=item.union(i))!=item:
                res.add(tmp)
    ans = res
평균 실행 시간 : 0.05 평균 메모리 사용량: 10.18
다른 사람의 풀이에서 본 풀이를 matched_user에 쓸 수 있도록 약간 내 방식으로 변형해 봤다
sol1의 line 25자리에 붙여 넣으면 된다
처음 봤을 때 이런 방법이 있구나 찐감탄했다
조합을 사용해서 선택하고 이중 for문을 이용하여 기존 요소에 합쳐준다
같은 불량 사용자 패턴이 여러 개일 경우, 시간이 늘어졌는데 이 방법을 사용하면 크게 단축할 수 있다
frozenset은 tuple처럼 변경 불가능한 set인 대신 set 안에 넣을 수 있다! 굿
'''