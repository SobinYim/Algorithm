def enc(x,n=1): #암호화 1 사이클
    res=0 if x[0]-n<1 else x[0]-n
    x.append(res)
    x.pop(0)
    if n==5 or res==0:
        return x
    else:
        enc(x,n+1)

for t in range(10):
    t=int(input()) #tc
    li=list(map(int,input().rstrip().split())) #숫자로 변환
    li=list(map(lambda x: x-(min(li)//30)*30,li)) #사이클이 30을 기준으로 반복되기 때문에 최솟값을 30으로 나눌 수 있는 몫만큼 전체 리스트에 나누어 줌
    while li[-1]: #li의 마지막 숫자가 0이 아니라면 암호화를 계속한다
        enc(li)
    print(f"#{t}",*li)