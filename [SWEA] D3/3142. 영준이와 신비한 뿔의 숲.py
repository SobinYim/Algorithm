T = int(input()) #tc 개수
for t in range(1,T+1):
    n,m=map(int, input().split()) #뿔의 개수, 짐승의 마리 수
    h=n-m #트윈혼
    u=m-h #유니콘
    print(f"#{t}",u,h)

'''
2h+u=n,h+u=m를 연립으로 정리하면 h=n-m, u=m-h
'''