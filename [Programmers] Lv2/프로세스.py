def solution(priorities, location): #실행 대기 큐에 있는 프로세스의 중요도, 몇 번째로 실행되는지 알고싶은 프로세스의 위치
    ans=1
    while priorities and location!=(mx:=priorities.index(max(priorities))): #priorities가 비어있지 않고 location이 최우선 프로세스가 아니라면 루프
        ans+=1
        priorities+=priorities[:mx]
        del priorities[:mx+1] #해당 프로세스를 앞으로 가져와서 처리
        if location>mx: #location의 위치 갱신
            location-=mx+1
        else:
            location+=len(priorities)-mx
    return ans

'''
평균 실행 시간 : 0.04 평균 메모리 사용량: 10.2

우선도 높은 프로세스를 찾아 꺼내는 과정을 반복하여 location이 나오는 시간을 구했다
deque의 rotate를 이용해 풀어도 된다(성능은 같았음)
'''