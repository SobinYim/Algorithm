T=int(input()) #tc 개수
seq=[1,1,1] #파도반 수열
for i in range(3, 100):
    seq.append(seq[i-3]+seq[i-2])
for t in range(1,T+1):
    n=int(input()) #p_n을 구하기 위한 n
    print(f"#{t}",seq[n-1])

'''
제출일 기준 python 실행시간 7위, 코드길이 7위
'''