#sol
from itertools import combinations
ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    n=map(int,input().split()) #정수 리스트
    res=sorted(set(map(sum,combinations(n,3))),reverse=True)[4] #combinations를 이용하여 nC3을 구하고 그 합을 set에 넣어 중복 제거
    ans.append(f"#{t} {res}")
for a in ans:
    print(a)

#sol2
ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    n=list(map(int,input().split())) #정수 리스트
    s=set() #조합의 합, 중복을 제거하기 위해 set
    for i in range(7): #첫 번째 선택
        for j in range(i+1,7): #두 번째 선택
            for k in range(j+1,7): #세 번째 선택
                s.add(n[i]+n[j]+n[k]) #선택한 수들의 합
    res=sorted(s,reverse=True)[4]
    ans.append(f"#{t} {res}")
for a in ans:
    print(a)

'''
sol은 itertools의 combinations 메서드를 이용하여 간편하게 구현하였고,
sol2은 for문을 이용하여 숫자를 선택하는 방식으로 조합을 구현하였음

제출일 기준 python 실행시간 1위(sol2), 코드길이 12위(sol)
'''