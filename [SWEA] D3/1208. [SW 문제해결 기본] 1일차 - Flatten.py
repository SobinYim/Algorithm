for t in range(10):
    n=int(input()) #덤프 수행 횟수
    li=list(map(int,input().rstrip().split())) #상자의 높이값
    for i in range(n): #최저점에는 1을 더하고 최고점에서 1을 빼주어 평탄화
        li[li.index(min(li))]+=1
        li[li.index(max(li))]-=1
    res=max(li)-min(li) #최고점과 최저점의 높이 차
    print(f"#{t+1}",res)