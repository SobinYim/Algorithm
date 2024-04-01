#sol1
for _ in range(10):
    t=int(input()) #tc
    x,m=map(int,input().split()) #x의 m승
    res=x**m
    print(f"#{t}",res)

#sol2 : 재귀
def sq(x,m):
    return x if m==1 else sq(x,m-1)*x
for _ in range(10):
    t=int(input()) #tc
    x,m=map(int,input().split()) #x의 m승
    res=sq(x,m)
    print(f"#{t}",res)