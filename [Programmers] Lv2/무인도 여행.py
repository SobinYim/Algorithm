def solution(maps): #지도
    visited = [[0] * (l := len(maps[0]) + 2) for _ in range(len(maps) + 2)] #방문 여부
    maps = ["X" * l] + [f"X{m}X" for m in maps] + ["X" * l] #패딩
    ans = [] #무인도에서 머물 수 있는 기간
    visit = set() #방문할 위치
    for i in range(1, len(maps)):
        for idx in range(l):
            if not visited[i][idx] and maps[i][idx] != "X": #아직 방문하지 않았고 해당 위치가 섬이라면
                visit.add((i, idx))
            tot = 0
            while visit:
                visit_this = set()
                for y, x in visit:
                    if maps[y][x] != "X":
                        tot += int(maps[y][x])
                        for c, r in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]: #상하좌우 탐색
                            if not visited[c][r]:
                                visit_this.add((c, r))
                    visited[y][x] = 1
                visit = visit_this
            if tot:
                ans.append(tot)
    return sorted(ans) if ans else [-1]


'''
평균 실행 시간 : 3.2 평균 메모리 사용량: 10.47

패딩을 주어 범위를 확인하지 않아도 된다
'''
