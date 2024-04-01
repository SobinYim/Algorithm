T=int(input()) #tc 개수
for t in range(1,T+1):
    print(f"#{t}",sum(map(int,input().split()))%24) #입력된 시간의 합을 24로 나눈 나머지 == 시간이 지난 후의 시각

'''
제출일 기준 python 코드길이 2위
'''