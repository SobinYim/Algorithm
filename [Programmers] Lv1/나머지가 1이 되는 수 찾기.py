def solution(n): #자연수 n
    answer=n-1 #소수일 때 x
    for i in range(2,int(n**.5)+1): #제곱근까지 검사했을 때 x가 없으면 소수
        if n%i==1:
            return i
    return answer

'''
평균 실행 시간 : 0.02 평균 메모리 사용량: 10.16
'''