T=int(input()) #tc 개수
for t in range(1,T+1):
    n,q=map(int,input().split()) #상자의 개수, 상자를 바꿀 횟수
    res=[0]*n #초기 상자
    for i in range(q):
        L,R=map(int,input().split()) #바꿀 상자의 시작과 끝 번호
        L-=1
        res[L:R]=[i+1]*(R-L) #L부터 R까지의 숫자 교체
    print(f"#{t}",*res)

'''
제출일 기준 python 실행시간 3위, 코드길이 2위
'''