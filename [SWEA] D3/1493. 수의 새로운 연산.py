def cal(n): # &n 연산 == n이 할당된 점 x,y를 구함
    for i,j in enumerate(li):
        if n<=j:
            break
    x=n-j+i+1
    y=j-n+1
    return x,y

li=[1]*285 #li[i] == sum(range(i+2)) == y축이 1인 값들의 모음
for i in range(1,285):
    li[i]+=li[i-1]+i
ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    p,q=map(int,input().split()) #연산을 위한 정수
    px,py=cal(p) # &연산으로 p의 x,y축 좌표를 계산
    qx,qy=cal(q) # &연산으로 q의 x,y축 좌표를 계산
    x=px+qx
    res=li[x+py+qy-3]+x
    ans.append(f"#{t} {res}")
for a in ans:
    print(a)

'''
대각선 순서로 수가 붙여진다는 점을 이용하여 풀었는데 풀 당시에는 이게 대각선이라 그렇다는 걸 알았다기보다는 그냥 규칙 찾아서 풀었다(ㅋㅋㅋ...)
처음에 y가 1인 구해준 리스트가 각 대각선의 최댓값
n보다 커지는 대각선 값(==n이 해당 대각선 안에 들어있음)을 찾아서 n과의 차를 구해줌
이 차는 곧 y축의 좌표 값이므로 y=j-n+1
x축은 y축이 늘어나면 줄어드므로 해당 대각선 값의 인덱스에서 n과의 차를 감해줌 x=n-j+i+1
1씩을 더해주는 것은 list의 인덱스가 0에서 시작하기 때문
같은 방식으로 x값과 y값을 모두 더한 값을 list에서 찾아준 후,
list에서 찾기 위해 x,y 값을 찾을 때 더해줬던 1을 처리해주었고, 이 값을 x값과 더하였음
정리하자면 li[px+qx+py+qy-3]+px+qx 인데, x값이나 y값이나 거기서 거기라 li[px+qx+py+qy-2]-(qy+py)+1로 찾을 수도 있다

제출일 기준 python 실행시간 1위
'''