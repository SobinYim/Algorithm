import heapq
def convert_min(t): #hh:mm 분으로 변환
    h, m = map(int, t.split(":"))
    return h * 60 + m
def solution(book_time): #대실 시작 시각, 대실 종료 시각
    ans = [float('inf')] #대실 중인 객실(사용 가능 시각)
    heapq.heapify(ans)
    for i in sorted(book_time): #체크인 빠른 순
        c_in, c_out = map(convert_min, i) #분으로 변환한 대실 시작 시각, 대실 종료 시각
        if ans[0] <= c_in: #대실 시작 시각에 대실이 종료된 객실이 있다면
            heapq.heappushpop(ans, c_out + 10) #최솟값 pop, 사용 가능 시각 push
        else:
            heapq.heappush(ans, c_out + 10) #사용 가능 시각 push
    return len(ans) - 1

'''
평균 실행 시간 : 1.07 평균 메모리 사용량: 10.46

드디어 풀 때 힙이 생각났다!
pushpop이 있어서 아주 편하고 좋았다
list로도 짜봤는데 약 2초가량 차이가 났다(아무래도 매번 정렬을 하니)
ans가 비어있는지 매번 검사하기 싫어서 inf 넣어놓고 return 할 때 1 빼주었다,, 와하핫

다른 사람에서 본 풀이:
def solution(book_time):
    answer = 0
    minute = [0 for _ in range(24*60 + 10)]
    for book in book_time:
        start,end=map(time2min,book)
        minute[start] += 1
        minute[end+10] += -1
    num = 0
    for i in range(len(minute)):
        num += minute[i]
        minute[i] = num
    answer = max(minute)
    return answer
평균 실행 시간 : 0.86 평균 메모리 사용량: 10.39
time2min은 convert_min과 같은 기능
타임 테이블을 만들어 놓고 누적합을 이용하여 최대 사용 객실 수를 구한다
깔끔하고 빠르고 아주 좋다!
'''
