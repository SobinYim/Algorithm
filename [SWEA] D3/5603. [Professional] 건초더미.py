T=int(input()) #tc 개수
for t in range(1,T+1):
    n=int(input()) #건초 더미 개수
    li=[0]*n
    for i in range(n):
        li[i]=int(input())
    avg=sum(li)/n
    res=int(sum(i-avg for i in li if i>avg)) # *
    print(f"#{t}",res)

'''
*
모두 같은 크기 == 평균값 이므로, 
평균과 평균보다 큰 크기의 건초(작은 크기의 건초여도 상관 X)의 차의 합이 곧 최소 움직임의 횟수가 됨
'''