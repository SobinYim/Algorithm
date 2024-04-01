def solution(n): #정수
    cnt=0 #시도 횟수
    while n!=1:
        if cnt==500: #500회 이상 시도
            return -1
        if n%2==0: #n이 짝수
            n//=2
        else: #n이 홀수
            n=n*3+1
        cnt+=1
    return cnt

'''
평균 실행 시간 : 0.03 평균 메모리 사용량: 10.15
'''