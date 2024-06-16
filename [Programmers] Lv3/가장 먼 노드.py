#sol
from collections import defaultdict
def solution(n, edge): #노드의 개수, 간선
    link = defaultdict(list) #인접 리스트
    for i, j in edge:
        link[i].append(j)
        link[j].append(i)
    visit = set([1]) #방문할 노드
    visited = set() #방문한 노드
    while visit:
        visit_next = set()
        ans = len(visit) #해당 step의 노드 수
        visited.update(visit)
        for i in visit:
            for node in link[i]:
                if node not in visited:
                    visit_next.add(node)
        visit = visit_next
    return ans

#sol1
from collections import defaultdict
def solution(n, edge): #노드의 개수, 간선
    link = defaultdict(list) #인접 리스트
    for i, j in edge:
        link[i].append(j)
        link[j].append(i)
    visit = [1] #방문할 노드
    visited = [0] * (n + 1) #방문 여부
    visited[1] = 1
    while visit:
        visit_next = []
        ans = len(visit) #해당 step의 노드 수
        for i in visit:
            for node in link[i]:
                if not visited[node]:
                    visited[node] = 1
                    visit_next.append(node)
        visit = visit_next
    return ans


'''
sol
평균 실행 시간 : 9.61 평균 메모리 사용량: 13.9
sol1
평균 실행 시간 : 8.11 평균 메모리 사용량: 13.42

sol, sol1은 같은 풀이
방문한 노드를 set로 저장하느냐 리스트로 방문 여부를 저장하느냐의 차이
i-1 해주기 번거로워서 한 칸 더 만들어줬다
생각보다 실행 시간 차이가 꽤 나서 좀 놀랍다
'''