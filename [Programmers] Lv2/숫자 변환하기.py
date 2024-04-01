#sol1
def solution(x, y, n): #x를 y로 변환, 가능한 연산에서 더할 수
    visited={y:0} #수:연산 횟수 딕셔너리
    stack=[y] #연산을 위해 순회할 수
    steps=0 #연산 횟수
    flag=True
    while flag: #flag가 True인 동안 루프
        tmp=[] #다음 steps의 stack
        steps+=1
        while stack:
            i=stack.pop()
            for j in [i/2,i/3,i-n]: #연산
                if not j%1 and j not in visited.keys() and j>=x: #연산한 수가 정수가 아니거나 이미 방문했거나 x보다 작아지면
                    visited[j]=steps
                    tmp.append(j)
                    if j==x: #연산한 수가 x라면 break
                        flag=False
                        break
        if not tmp: #다음 steps가 없다면 break
            break
        stack=tmp
    return visited.get(x,-1)

#sol2
from collections import deque
def solution(x, y, n): #x를 y로 변환, 가능한 연산에서 더할 수
    if x==y:
        return 0
    visited=[] #이미 방문한 수
    visit_dq=deque([(float(y), 0)]) #연산을 위해 순회 (수, 연산 횟수)
    while visit_dq: #visit_dq가 존재하는 동안 루프
        i, steps = visit_dq.popleft() #bfs를 위해 먼저 들어온 요소부터 pop
        for j in [i/2, i/3, i-n]: #연산
            if j.is_integer() and j not in visited and j>=x: #연산한 수가 정수가 아니거나 이미 방문했거나 x보다 작아지면
                if j==x: #연산한 수가 x라면 return steps+1
                    return steps+1
                visit_dq.append((j, steps+1))
    return -1

'''
#sol1
평균 실행 시간 : 0.22 평균 메모리 사용량: 10.25
#sol2
평균 실행 시간 : 9.65 평균 메모리 사용량: 11.21

sol2>sol1 순으로 작성했다
sol1과 sol2 모두 y부터 시작하여 x를 찾는다
이는 곱셈 연산이 나눗셈 연산이 되어 x부터 시작했을 때 쓸 데 없는 연산을 하는 것을 미연에 방지하기 위함이다

sol1은 딕셔너리를 이용하여 이미 방문한 수를 저장한다
다음 steps의 수를 따로 저장하여 연산 횟수를 stack에 같이 저장할 필요가 없다
사실 그래서 steps 값이 필요하지 않아 list를 써도 무관하지만 연산한 수가 이미 방문했는지를 매번 확인하기 때문에 딕셔너리 쪽이 나을 거라고 생각했다
get을 이용할 수 있기도 하고 x와 y가 같은 경우를 따로 처리하지 않아도 돼서 여러모로 편하기도 하고!
또 while을 두 번 쓰는데,, while stack 말고 for문도 써봤지만 pop을 쓰는 while이 더 느릴 거라는 생각과는 달리 큰 차이 없었다
루프-루프-순회 구조라 조금 그런가 싶긴 하지만,,

sol2는 deque를 이용하여 순회할 수와 연산 횟수를 저장했다
넓이 우선 탐색이므로 steps가 어느 쪽이 더 작은지 비교할 필요가 없다,, 그냥 방문했다면 stack에 추가하지 않으면 된다
while visit_dq 하나라 sol1보다 안정적으로 느껴진다,,
속도 차이는 조금 크게 나긴 하지만 sol1이 빠른 거지 sol2가 느린 게 아니다,,,,,
'''