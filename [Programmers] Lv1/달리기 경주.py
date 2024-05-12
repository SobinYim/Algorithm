#sol
def solution(players, callings):
    player_rank=dict((p,idx) for idx,p in enumerate(players))
    for i in callings:
        c=player_rank[i]
        players[c],players[c-1]=players[c-1],players[c]
        player_rank[i]-=1
        player_rank[players[c]]+=1
    return players

#sol1
def solution(players, callings):
    player_rank=dict((p,idx) for idx,p in enumerate(players))
    for i in callings:
        c=player_rank[i]
        players[c],players[c-1]=players[c-1],players[c]
        p=players[c]
        player_rank[i],player_rank[p]=player_rank[p],player_rank[i]
    return players

'''
sol
평균 실행 시간 : 138.14 평균 메모리 사용량: 30.3
sol1
평균 실행 시간 : 120.39 평균 메모리 사용량: 30.23

테케 9에서 100ms에 달하는 걸 보고 기겁해서 다양한 시도들을 해봤으나,, 이 방법이 제일 빨랐다
sol과 sol1은 player_rank 딕셔너리 값 변경 로직(스왑/값에+-1) 차이다
다른 사람의 풀이를 보니까 인덱스를 저장해 두고 할당하는 방식이 가장 빨랐다 
'''