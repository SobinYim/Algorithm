def solution(n): #자연수
    answer=[]
    while n: #각 자릿수 리스트에 추가(일의 자리부터 들어가서 따로 뒤집어줄 필요가 없다)
        answer.append(n%10)
        n//=10
    return answer

def solution(n): #자연수
    answer=list(map(int,str(n)))[::-1] #문자형으로 바꾼 n의 각 자릿수를 int형 변환한 것을 뒤집는다
    return answer

'''
#sol1
평균 실행 시간 : 0.0 평균 메모리 사용량: 10.19
#sol2
평균 실행 시간 : 0.02 평균 메모리 사용량: 10.36

역시 형 변환보다 수 연산이 훨 빠르다
'''