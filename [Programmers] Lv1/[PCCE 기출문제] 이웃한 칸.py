def solution(board, h, w): #칸마다 색이 칠해진 2차원 격자 보드판, y위치, x위치
    n=0
    color=board[h][w]
    lh,lw=len(board),len(board[0])
    coord=[[h,w-1],[h,w+1],[h-1,w],[h+1,w]] #탐색할 위치
    for y,x in coord:
        if 0<=y<lh and 0<=x<lw: #board 범위 안이라면
            n+=(color==board[y][x])
    return n

'''
평균 실행 시간 : 0.001 평균 메모리 사용량: 10.176
'''