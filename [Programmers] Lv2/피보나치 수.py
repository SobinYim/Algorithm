def solution(n): #자연수
    x,y=0,1
    for i in range(n):
        x,y=y,(x+y)%1234567
    return x

'''
평균 실행 시간 : 1.15 평균 메모리 사용량: 10.12

x,y=0,1로 두고 range(n)을 해도 되고
x,y=1,1로 두고 range(n-1)을 해도 되고
x,y=1,2로 두고 range(n-2)를 해도 되고
취향에 따라,, 쓰면 되겠다,,, 물론 그 이상은 안됨
'''