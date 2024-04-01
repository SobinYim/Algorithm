def solution(x): #양의 정수
    n=sum(map(int,str(x))) #각 자리수를 int형으로 변환한 것의 합
    answer = x%n==0 #x를 n으로 나눌 수 있는지
    return answer

'''
평균 실행 시간 : 0.02 평균 메모리 사용량: 10.32
'''