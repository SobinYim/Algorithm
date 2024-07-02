#sol
def solution(sequence, k): #수열, 부분 수열의 합
    mx = len(sequence) - 1 #부분 수열의 시작 인덱스(큰 수부터 들어가므로 부분 수열의 최댓값 인덱스)
    tot = 0 #부분 수열의 합
    for i in range(len(sequence) - 1, -1, -1):
        val = sequence[i]
        if val > k: #목푯값보다 크다면 continue
            mx -= 1
            continue
        tot += val
        if tot == k: #부분 수열의 합이 목표했던 값과 같다면
            if val == sequence[mx]: #부분 수열이 숫자 하나로만 구성된다면
                return [sequence.index(val), sequence.index(val) + k // val - 1]
            else:
                return [i, mx]
        while tot > k: #부분 수열의 합계가 목푯값보다 크다면 루프
            tot -= sequence[mx]
            mx -= 1
    return [0, 0]

#sol1
from collections import deque
def solution(sequence, k): #수열, 부분 수열의 합
    elem = deque() #부분 수열 인덱스
    tot = 0 #부분 수열의 합
    for i in range(len(sequence) - 1, -1, -1):
        val = sequence[i]
        if val > k: #목푯값보다 크다면 continue
            continue
        tot += val
        elem.append(i)
        if tot == k: #부분 수열의 합이 목표했던 값과 같다면
            if sequence[elem[-1]] == sequence[elem[0]]: #부분 수열이 숫자 하나로만 구성된다면
                return [sequence.index(val), sequence.index(val) + k // val - 1]
            else:
                return [elem[-1], elem[0]]
        while tot > k: #부분 수열의 합계가 목푯값보다 크다면 루프
            tot -= sequence[elem.popleft()]
    return [0, 0]


'''
sol
평균 실행 시간 : 30.37 평균 메모리 사용량: 20.95
sol1
평균 실행 시간 : 42.44 평균 메모리 사용량: 25.87

sol과 sol1는 기본적으로 같은 풀이이다
부분 수열의 인덱스를 list로 관리하느냐 int형으로 관리하느냐의 차이 
sol1을 먼저 짰는데 idx를 배열의 형태로 저장할 필요가 없을 것 같아서 sol를 짜게 되었다
배열이 아닌 int형으로 불필요한 동작을 줄이니 자원 소모량이 확실히 줄었다

가장 짧은 구간을 반환하기 위해 뒤에서부터 순회하며 더하고
더한 값이 k보다 커지면 부분 수열의 범위를 줄인다
k와 같아지면 [현재 인덱스, 최댓값 인덱스]를 반환한다
단, 부분 수열의 구성 요소가 모두 같다면 잘못된 인덱스를 반환하므로 [sequence.index(현재 요소), sequence.index(현재 요소)+(k//현재 요소)]를 반환한다.
 
처음에는 Counter를 이용해 보려고 했는데 뭔가 생각처럼 잘 안 풀려서 현재 풀이로 틀었다
'''