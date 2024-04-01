def solution(board, moves): #게임 보드, 크레인 움직임
    basket=[] #바구니
    board=list(map(list,zip(*board))) #전치
    board=[list(filter(lambda x: x>0,item)) for item in board] #빈 값 제거
    answer=0
    for move in moves:
        if not board[move-1]: #칸이 비어있을 경우
            continue
        item=board[move-1].pop(0) #인형 뽑기
        if basket and basket[-1]==item: #같은 인형이 연속으로 쌓일 경우
            basket.pop()
            answer+=2
        else:
            basket+=[item]
    return answer
'''
평균 실행 시간 : 0.1 평균 메모리 사용량: 10.21

속도도 잘 나오고 깔끔하게 잘 짜인 것 같아서 마음에 든다!
한 가지 아쉬운 건 board 부분에서 전치와 빈 값 제거를 한 번에 할 수 있었는데 생각을 못 한 것 정도
그래도 보기에 편하기도 하고, 성능에 큰 영향을 주는 건 아니니 그냥 내버려두기로
'''