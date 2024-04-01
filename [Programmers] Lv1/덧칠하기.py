def solution(n, m, section): #벽의 길이, 롤러의 길이, 칠해야 하는 구역
    painted,answer=0,0
    for i in section:
        if i<painted:
            continue
        else:
            painted=i+m
            answer+=1
    return answer

'''
평균 실행 시간 : 0.92 평균 메모리 사용량: 10.94
'''