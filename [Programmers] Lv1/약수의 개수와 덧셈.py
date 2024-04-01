#sol1
sq=[i**2 for i in range(1,32)] #1~1000 사이의 제곱수
def solution(left, right): #시작, 끝
    answer=(right-left+1)/2*(left+right)-(sum(filter(lambda x: left<=x<=right,sq))*2)
    return answer

#sol2
def solution(left, right): #시작, 끝
    answer=0
    for i in range(left,right+1):
        if i**.5%1==0: #약수가 홀수 == 제곱근이 정수
            answer-=i
        else: answer+=i
    return answer

'''
#sol1
평균 실행 시간 : 0.01 평균 메모리 사용량: 10.16
#sol2
평균 실행 시간 : 0.12 평균 메모리 사용량: 10.18

sol1은 left~right의 합에 그 사이에 존재하는 제곱수의 합에 2를 곱하여 빼준 것(빼야할 것을 더했으니까)
sol2는 left~right 사이의 수를 순회하며 제곱근이 정수인지 검사하고 정수라면 빼고 아니라면 더한다
'''