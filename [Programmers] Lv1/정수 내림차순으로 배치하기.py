#sol1
def solution(n): #정수
    num=[]
    while n: #각 자리수를 리스트에 추가
        num+=[n%10]
        n//=10
    answer=sum([item*10**digit for digit,item in enumerate(sorted(num))]) #정렬 후 idx==자릿수 이므로 10**idx를 각 요소에 곱한 것의 합
    return answer

#sol2
def solution(n): #정수
    answer=int("".join(sorted(str(n), reverse=True))) #문자형 변환 후 정렬한 것을 int형 변환
    return answer

'''
#sol1
평균 실행 시간 : 0.01 평균 메모리 사용량: 10.22
#sol2
평균 실행 시간 : 0.02 평균 메모리 사용량: 10.32
'''