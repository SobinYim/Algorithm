ans=[]
T = int(input())
for t in range(1,T+1):
    u,a,b=map(int, input().rstrip().split()) #표본 수, a채널을 구독하고 있는 사람 수, b채널을 구독하고 있는 사람 수
    maxn=min(a,b) #최대가 되려면 더 작은 쪽이 큰 쪽의 부분 집합이어야 함
    minn=a+b-u #최소는 두 집단의 합에서 표본 수를 뺀 값
    minn=minn if minn>0 else 0
    ans.append(f"#{t} {maxn} {minn}")
for a in ans:
    print(a)

'''
제출일 기준 python 실행시간 3위
'''