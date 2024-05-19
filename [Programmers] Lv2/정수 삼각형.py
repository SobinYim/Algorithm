#sol1
def solution(triangle): #정수 삼각형
    prev = triangle.pop(0) #이전 각 루트의 최댓값
    for i, t in enumerate(triangle):
        for idx, item in enumerate(t):
            t[idx] += prev[0] if not idx else prev[-1] if idx > i else max(prev[idx - 1:idx + 1]) #양쪽 끝은 끝을, 중간은 큰 값을 선택하여 더함
        prev = t
    return max(prev)

#sol2
def solution(triangle): #정수 삼각형
    prev = triangle.pop() #이전 각 루트의 최댓값
    for t in triangle[::-1]:
        for j in range(len(t)):
            t[j] += max(prev[j:j + 2])
        prev = t
    return prev[0]

'''
sol1
[효율성 테스트] 평균 실행 시간 : 32.27 평균 메모리 사용량: 14.16
sol2
[효율성 테스트] 평균 실행 시간 : 28.2 평균 메모리 사용량: 14.06

sol1은 위에서부터 내려가고, sol2는 밑에서부터 올라간다
어느 쪽을 선택하느냐는 취향 차 같다

다른 사람의 풀이:
def solution(t, l=[]):
    for r in t: l=[max(t,y)+z for t,y,z in zip([0]+l,l+[0],r)]
    return max(l)
[효율성  테스트] 평균 실행 시간 : 21.79 평균 메모리 사용량: 14.16
패딩을 왼쪽과 오른쪽에 넣어 따로 처리할 필요 없이 값 비교를 할 수 있다
내려가면서 왼쪽/오른쪽 중 큰 값을 더해준다
심플하면서 명료하고 성능도 굿
'''