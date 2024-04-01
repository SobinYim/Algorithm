def solution(x, n): #x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트
    return [0]*n if x==0 else list(range(x,x*(n+1),x))

'''
평균 실행 시간 : 0.02 평균 메모리 사용량: 10.25

왜 lv0이 아닌지 모를 문제
'''