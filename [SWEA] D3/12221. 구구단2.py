T=int(input()) #tc 개수
for t in range(1,T+1):
    n1,n2=map(int,input().split()) #정수
    res= n1*n2 if 0<n1<10 and 0<n2<10 else -1 #n1과 n2가 1~9 사이라면 곱셈을 아니라면 -1을 저장
    print(f"#{t}",res)

'''
제출일 기준 python 코드길이 7위
'''