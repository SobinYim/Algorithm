def solution(a, b): #정수 배열 a,b
    answer=sum(map(lambda x,y: x*y,a,b))
    return answer

'''
평균 실행 시간 : 0.08 평균 메모리 사용량: 10.27

map을 썼지만 zip을 써도 되는 문제
사실 zip을 쓰는 편이 더 빠르다
'''