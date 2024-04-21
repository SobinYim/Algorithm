def solution(m, n, puddles): #m*n 크기의 격자, 물에 잠긴 지역의 위치
    m,n=m+1,n+1
    metrix=[[0]*m for _ in range(n)] #해당 위치로 갈 수 있는 경우의 수
    metrix[0][1]=1 #(1,1)에서 1로 시작하기 위함
    for y in range(1,n):
        for x in range(1,m):
            if [x,y] in puddles:
                continue
            else:
                metrix[y][x]=(metrix[y-1][x]+metrix[y][x-1])%1000000007 #해당 위치로 올 수 있는 경우의 수의 합
    return metrix[-1][-1]

'''
[효율성  테스트] 평균 실행 시간 : 2.09 평균 메모리 사용량: 10.27

DP 문제인데 DP로 풀겠다는 생각보다는,,, 이거 확통 문제네 싶었다
metrix[0][1]=1 이 부분은 metrix[1][0]=1 이어도 무방
다른 사람의 풀이를 보니까 웅덩이를 미리 처리하면 시간을 감축시킬 수 있는 것 같다
이 문제에서는 puddles가 10개 이하라 크게 차이는 안 나지만 puddles가 커지면 아무래도 in연산이라 차이가 더 크게 벌어질 것 같다
'''