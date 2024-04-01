ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    n=int(input()) #상자의 개수
    res=0 #결과 값 초기화
    for i in range(n):
        p,s=map(float,input().split()) #확률과 값
        res+=p*s #평균 값은 ps의 합이므로
        ans.append(f"#{t} {res}")
    for a in ans:
        print(a)

'''
제출일 기준 python 실행시간 3위
'''