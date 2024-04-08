from itertools import chain
def solution(n): #정수 n
    ans=[[i]*i for i in range(1,n+1)] #피라미드 매트릭스
    n_end=n+1
    q=0
    for i in range(1,n):
        n_start,n_end=n_end,n_end+n-i
        li=range(n_start,n_end) #채울 숫자
        if not i%3: #아래로 내려가며 채우기
            for number,idx in zip(li,range(2*q,n-q)):
                ans[idx][q]=number
        elif i%3==1: #행 구간 채우기
            ans[-q-1][q+1:n-q*2]=list(li)
        else: #위로 올라가며 채우기
            q+=1
            for number,idx in zip(li,range(n-(q+1),2*(q-1),-1)):
                ans[idx][-q]=number
    return list(chain(*ans)) #중첩 리스트 병합하여 반환

'''
평균 실행 시간 : 20.04 평균 메모리 사용량: 21.3

로직은 간단하다! 그냥 방향 따라 돌아가면서 채워주었다
중첩 리스트를 평탄화할 때 컴프리헨션으로 [i for item in ans for i in item]를 써도 되는데
아무래도 for문 두 번이라 가독성에서 좋지 않은 것 같아서 chain을 사용했다
실행 시간에 차이는 크게 없었다
다른 사람의 풀이에서 sum(ans,[])를 사용하는 것도 봤는데 속도가 느리기는 하지만 처음 보는 방식이라 신기했다
ans는 중첩 리스트고 두 번째 인자인 []가 초기 상태라 한다
q도 i//3을 써도 되지만 인덱스에서 -q-1을 매번 연산하는 게 비효율인 것 같아서 올라갈 때 q+=1을 해주었다
이 풀이가 확인했던 풀이 중에서는 제일 빠르기는 하지만 조금 더 깔끔 간결하게 짜고 싶은 아쉬움도 있다

from itertools import chain
def solution(n):
    [row, col, cnt] = [-1, 0, 1]
    board = [[None] * i for i in range(1, n+1)]
    for i in range(n):
        for _ in range(n-i):
            if i % 3 == 0:
                row += 1
            elif i % 3 == 1:
                col += 1
            else:
                row -= 1
                col -= 1
            board[row][col] = cnt
            cnt += 1
    return list(chain(*board))
평균 실행 시간 : 38.47 평균 메모리 사용량: 21.28
다른 사람의 풀이에서 본 풀이!
내 풀이와 매커니즘은 같다
첫 번째 for문은 진행 횟수이고 두 번째 for문은 채울 숫자의 수이다
내 풀이에서는 for문을 만들어서 풀었다면 이 풀이에서는 채울 방향에 따라 행과 열의 위치를 옮기며 행렬에 넣어준다
또 차이점이라면 내 풀이에서는 방향이 바뀔 때 채울 방법을 선택한다면 이 풀이에서는 모든 요소에서 방향을 확인한다는 점
아마 여기에서 실행 시간 차이가 생기는 것 같다
어떻게 보면 진정한 달팽이 채우기..
속도도 빠르고 심플해서 좋다!
'''