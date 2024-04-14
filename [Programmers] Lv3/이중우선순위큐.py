#sol1
import heapq
def solution(operations): #연산 [명령어, 높이]
    hq=[]
    heapq.heapify(hq)
    for i in operations:
        c,n=i.split()
        if c=="D": #삭제
            if not hq:
                continue
            if n=="1": #최댓값
                hq.remove(max(hq))
                heapq.heapify(hq)
            else: #최솟값
                heapq.heappop(hq)
        else: #삽입
            heapq.heappush(hq,int(n))
    if not hq:
        hq=[0]
    return [max(hq),hq[0]]

#sol2
def solution(operations): #연산 [명령어, 높이]
    li=[]
    for i in operations:
        c,n=i.split()
        if c=="D": #삭제
            if not li:
                continue
            if n=="1": #최댓값
                li.pop()
            else: #최솟값
                li.pop(0)
        else: #삽입
            li.append(int(n))
            li.sort()
    if not li:
        li=[0]
    return [li[-1],li[0]]

#sol3
from collections import deque
def solution(operations): #연산 [명령어, 높이]
    dq=deque()
    for i in operations:
        c,n=i.split()
        if c=="D": #삭제
            if not dq:
                continue
            if n=="1": #최댓값
                dq.pop()
            else: #최솟값
                dq.popleft()
        else: #삽입
            n=int(n)
            if not dq:
                dq.append(n)
                continue
            for idx,item in enumerate(dq):
                if item>n:
                    break
            else:
                dq.append(n)
                continue
            dq.insert(idx,n)
    if not dq:
        dq=[0]
    return [dq[-1],dq[0]]

'''
#sol1
평균 실행 시간 : 0.025 평균 메모리 사용량: 10.283
#sol2
평균 실행 시간 : 0.02 평균 메모리 사용량: 10.216
#sol3
평균 실행 시간 : 0.027 평균 메모리 사용량: 10.35

sol2와 sol3은 사실 이런 풀이도 통과가 된다고?? 하면서 짠 것에 가깝기는 하다,,
효율은 sol1=sol2>>>sol3이 되겠다
sol1은 힙을 사용하기는 했는데 max를 써서 케이스가 커지면 다소 느려질 것 같고,,
구조를 유지하기 위해 다시 heapify를 해줘야 한다,,
테스트 케이스가 많이 작은지 sol2가 sol1보다 빨랐다
케이스가 좀 더 커지면 실행 시간 차이가 어떻게 나오는지 보고 싶은데 참 아쉽다
정석 풀이는 최대힙, 최소힙 쓰고 동기화 시키는 거라 한다,,
다른 사람의 풀이에서 이진 트리부터 구현한 사람이 있었는데 대단,,
'''