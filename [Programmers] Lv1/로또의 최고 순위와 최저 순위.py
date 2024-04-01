def solution(lottos, win_nums): #알 수 있는 로또 번호, 당첨 번호
    matched_n=len([i for i in lottos if i in win_nums]) #일치 개수
    unknown_n=lottos.count(0) #알 수 없는 번호 개수
    min_rank=7-matched_n
    return [min(min_rank-unknown_n,6),min(min_rank,6)]

'''
평균 실행 시간 : 0.004 평균 메모리 사용량: 10.18
'''