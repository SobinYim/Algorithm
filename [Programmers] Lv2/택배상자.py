#sol1
def solution(order): #택배 기사님이 원하는 상자 순서
    container = 0 #보조 컨테이너 상자 수
    for idx, i in enumerate(order):
        if container < (tmp := i - idx):
            container = tmp
        elif i < container:
            return idx
        container -= 1
    return len(order)

#sol2
def solution(order): #택배 기사님이 원하는 상자 순서
    mx = 0 #트럭에서 나간 상자 수
    container = [] #보조 컨테이너
    for idx, i in enumerate(order):
        if i > mx:
            container.extend(range(mx + 1, i))
            mx = i
        elif i != container.pop():
            return idx
    return len(order)


'''
sol1
평균 실행 시간 : 27.8 평균 메모리 사용량: 33.41
sol2
평균 실행 시간 : 72.37 평균 메모리 사용량: 39.31

sol1>sol2 순으로 짰다

보조 컨테이너를 배열 형태로 만들지 않아도 충분히 풀 수 있는 문제다!
실제로 sol1은 보조 컨테이너를 만들지 않고 계산하여 푼 풀이다
상자를 트럭에 바로 싣기 위해서는 상자의 위치 i가 idx와 보조 컨테이너에 실린 택배 수의 합보다 커야 하고
보조 컨테이너의 택배를 싣기 위해서는 i가 보조 컨테이너 벨트의 택배 수보다 작지 않아야 한다
컨테이너는 i-idx인데 이는 i는 필요한 상자의 위치이고 idx는 지금까지 트럭에 실은 상자의 개수이기 때문(==꺼냈지만 트럭에 싣지 않은 상자)
다시 말해 idx+컨테이너는 주 컨테이너에서의 최소 인덱스, 컨테이너 수는 보조 컨테이너에서의 최소 인덱스인 셈이다

sol2는 컨테이너를 만들어서 해결한 풀이로
보조 컨테이너에는 상자의 위치 최댓값 갱신 시 이전 최댓값+1~현재 상자의 위치가 들어가므로 extend와 range를 이용했다
최댓값 갱신이 아닐 시에는 보조 컨테이너에 적재된 택배라는 뜻이므로 pop()으로 꺼내온 위치가 현재 위치가 아니라면 return idx

1 페이지에서 가장 빠른 풀이도 케이스 5까지 평균 18.19ms 정도 걸리는 데 반해 보조 컨테이너 벨트를 만들지 않으면 0.01ms 안으로 끝난다(sol2는 14.82ms)
원래는 return len(order) 부분이 return idx+1였는데 idx가 for문 안에서 선언되어서 그냥 바꿔줬다
'''