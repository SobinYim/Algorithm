from math import ceil
ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    n,d=map(float,input().split()) #정원의 크기, 분무기가 물을 줄 수 있는 구간
    d=2*d+1 #분무기의 크기
    res=ceil(n/d) #필요한 분무기의 수
    ans.append(f"#{t} {res}")
for a in ans:
    print(a)

'''
제출일 기준 python 실행시간 5위
'''