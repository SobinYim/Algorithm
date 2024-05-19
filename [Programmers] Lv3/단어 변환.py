def solution(begin, target, words): #시작 단어, 타겟 단어, 단어의 집합
    visited = set() #방문한 단어
    step = 0 #단계
    visit = set([begin]) #방문할 단어
    while visit: #방문할 단어가 있다면 루프
        visit_this = set() #다음 step에서 방문할 단어
        step += 1
        for tg in visit: #검사 중인 단어
            visited.add(tg) #방문한 단어에 저장
            for word in words:
                if word not in visited: #word를 아직 방문하지 않았다면
                    cnt = 0
                    for t, w in zip(tg, word):
                        if t != w:
                            cnt += 1
                        if cnt > 1: #tg와 word가 다른 부분이 2곳 이상이라면 break
                            break
                    else: #tg와 다른 부분이 1곳이라면
                        if word == target: #word가 타겟 단어라면 step 반환
                            return step
                        visit_this.add(word)
        visit = visit_this
    return 0

'''
평균 실행 시간 : 0.04 평균 메모리 사용량: 10.24

까다로운 부분이 없어서 생각보다 무난하게 풀렸던 문제
다른 풀이들이랑 로직이 크게 다르지 않은데 실행 시간 차이가 좀 났다(두 배 이상)
왜 빠르지 set 차이인가...???
'''