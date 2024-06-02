from collections import deque
def solution(n, computers): #컴퓨터의 개수, 연결 정보
    visited = [0] * n #방문한 노드
    visit = deque() #방문할 노드
    network = 0 #네트워크의 수
    for i in range(n):
        if visited[i]: #이미 방문했다면 continue
            continue
        visit.append(i)
        while visit:
            node = visit.popleft()
            for j in range(n):
                if not visited[j] and computers[node][j]: #아직 방문하지 않았고, 연결된 노드라면 방문 리스트에 추가
                    visit.append(j)
                    visited[j] = 1
        network += 1
    return network


'''
평균 실행 시간 : 0.1 평균 메모리 사용량: 10.21

문제에서는 대칭 행렬이 input으로 주어져서 문제가 없지만
비대칭 행렬에서는 제대로 작동하지 않는다...
유니온-파인드를 사용하면 비대칭 행렬에서도 제대로 작동한다
루트 노드를 찾아서 병합하는 알고리즘으로 연결성을 확인하거나 사이클 존재 여부를 검사하는 데 사용된다고 한다
근데 이 방법도 연결 전체를 확인해야지 이미 확인한 구간을 건너뛰거나 하면 DFS/BFS 결과와 다르지 않게 나온다

위 코드에서는 for문으로 순회하며 이미 방문했는지 검사했는데 
다른 풀이 보니까 visited에서 0의 위치를 찾아 방문할 수도 있다

인상 깊었던 다른 사람에서 풀이:
def solution(n, computers):
    for i in range(n):
        searched = [c for c in computers if c[i]>0]
        computers = [c for c in computers if not c[i]]
        merged = [sum(e) for e in zip(*searched)]
        computers.append(merged)
    return len(computers)
평균 실행 시간 : 0.36 평균 메모리 사용량: 10.14
원풀이에서는 filter를 썼는데 리스트 컴프리헨션으로 바꿨다
굉장히 독특했던 풀이,, 이 코드대로라면 가독성 신경 안 쓰고 한 줄로 끝내버릴 수 있다
유니온-파인드의 접근법을 활용하여 비대칭 행렬에서도 제대로 작동한다
더 정확히 설명하자면 연결된 노드들을 분리하여 병합 후, 연결 정보(computers)에 다시 추가한다

return len([(computers:=[c for c in computers if not c[i]]+[[sum(e) for e in zip(*[c for c in computers if c[i]>0])]]) for i in range(n)][-1])
평균 실행 시간 : 0.34 평균 메모리 사용량: 10.15
ㅋㅋ
좀 많이 더럽긴 한데 가능은 하다~ 정도
'''

