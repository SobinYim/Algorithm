ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    d,a,b,f=map(int,input().split()) #두 기차 전면부 사이의 거리, 기차 a의 속력, 기차 b의 속력, 파리의 속력
    res=d/(a+b)*f #열차가 충돌하기까지 걸리는 시간*파리의 속력
    ans.append(f"#{t} {res}")
for a in ans:
    print(a)

'''
제출일 기준 python 실행시간 1위
'''