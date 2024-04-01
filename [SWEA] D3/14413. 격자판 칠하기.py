ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    n,m=map(int,input().split()) #격자판의 크기
    li=[""]*n #격자판
    for i in range(n): #격자판 입력
        li[i]=input()
    e,o=set(),set() #짝수 칸, 홀수 칸의 집합
    res="possible"
    for i,j in enumerate(li):
        e=e.union(set([j[k] for k in range(i%2,m,2)])) #i를 2를 나눈 나머지를 사용하여 매 행마다 위치를 바꿔 격자판을 만든 것을 집합으로 중복 제거
        o=o.union(set([j[k] for k in range((i+1)%2,m,2)]))
        e.discard("?") #와일드 카드 제거
        o.discard("?")
        if len(e.intersection(o))!=0 or 1<len(e) or 1<len(o): #각 집합의 길이가 2 이상이거나 교집합이 존재할 경우 "impossible", break
            res="impossible"
            break
    ans.append(f"#{t} {res}")
for a in ans:
    print(a)

'''
제출일 기준 python 실행시간 2위, 코드길이 8위, 메모리 1위
'''