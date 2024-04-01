ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    a,b,c,d=map(int,input().split()) #전구 x: a~b초, 전구 y: c~d초
    res=0 if min(b,d)-max(a,c)<0 else min(b,d)-max(a,c)
    ans.append(f"#{t} {res}")
for a in ans:
    print(a)

'''
동시에 켜진 시간은 전구 x가 켜진 초와 y가 켜진 시간의 교집합이므로
빨리 꺼진 전구의 초와 늦게 켜진 전구의 초의 차와 같음
'''