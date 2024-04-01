from math import isqrt
def solution(brown, yellow): #갈색 격자, 노란색 격자 수
    n=(brown-4)//2
    for i in range(1,isqrt(yellow)+1):
        if yellow%i==0 and yellow//i+i==n:
            return [yellow//i+2,i+2]
'''
평균 실행 시간 : 0.03 평균 메모리 사용량: 10.22

brown=2x+2y+4, yellow=x*y
이를
x+y=n, x*y=yellow
로 만들어서 풀었다..
폭과 높이는 [x+2,y+2]

def solution(brown, yellow):
    m=brown+yellow
    s=(brown+4)//2
    diff=(s//2)
    x=diff//2
    y=s-x
    diff//=2
    while x*y!=m:
        if diff!=1:
            diff//=2
        if x*y>m:
            x-=diff
            y+=diff
        else:
            x+=diff
            y-=diff
    return [y, x]
이분 탐색을 이용한 풀이법! 무지 빠르다!(0.006ms)

import math
def solution(brown, yellow):
    w = ((brown+4)/2 + math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    h = ((brown+4)/2 - math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    return [w,h]
근의 공식을 이용해서 깔끔하게 풀었다..
'''