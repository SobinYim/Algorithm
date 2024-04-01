#sol
ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    n=int(input()) #주어질 정수의 개수
    li=sorted(map(int,input().split()),reverse=True) #정수 리스트 내림차순 정렬
    res=-1 #결과 기본값
    for i in range(n-1):
        for j in range(i+1,n):
            m=li[i]*li[j] #숫자 선택
            if res>m: #이미 있는 res보다 곱한 값이 작으면 이후로는 검사할 필요 없음
                break
            temp=48 #비교를 위한 임시 값 초기화
            for k in str(m): #ord를 이용하여 숫자 비교, 단조 증가하는 수가 아니라면 continue
                if ord(k)<temp:
                    temp=48
                    break
                temp=ord(k)
            if temp==48:
                continue
            res=m
    ans.append(f"#{t} {res}")
for a in ans:
    print(a)

#sol2
from itertools import combinations
ans=[]
T=int(input())
for t in range(1,T+1):
    n=int(input())
    li=list(map(int,input().split()))
    mli=sorted(map(lambda x: x[0]*x[1],combinations(li,2)),reverse=True)
    for i in mli:
        exec(f'res={"<=".join(str(i))}')
        if res:
            break
    ans.append(f"#{t} {i}")
for a in ans:
    print(a)

'''
sol2는 exec 함수가 막혀있어서 제출하진 못했지만, 이왕 짰으니 저장
'''