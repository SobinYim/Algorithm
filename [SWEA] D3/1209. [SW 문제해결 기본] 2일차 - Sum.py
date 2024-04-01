for t in range(10):
    n=int(input()) #tc 번호
    li=[]
    d,d_=0,0
    for i in range(100):
        t=list(map(int,input().split())) #행을 숫자로 변환시켜 받아줌
        li.append(t)
        d+=t[i] #대각선의 합을 계산하기 위함 : i행의 i번째 요소
        d_+=t[-i] #위와 방향을 제외하고 동일함
    li_t=max(map(sum,zip(*li))) #전치행렬의 각 행의 합(==각 열의 합)의 최댓값
    res=max(*map(sum,li),li_t,d,d_) #각 행의 합, 열의 합, 각 대각선의 합 중 최댓값
    print(f"#{n}",res)

'''
zip(*li)를 이용해 전치행렬을 만들 수 있음
단, 튜플 형태이므로 리스트 형태가 필요하다면
list(map(list,zip(*li))) 등으로 변환시켜주어야 함
'''