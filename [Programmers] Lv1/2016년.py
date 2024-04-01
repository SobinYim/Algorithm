#sol1
def solution(a, b): #월, 일
    ca=[31,29,31,30,31,30,31,31,30,31,30,31] #2016년은 윤년
    wd=["THU","FRI","SAT","SUN","MON","TUE","WED"] #요일
    answer=wd[sum(ca[:a-1]+[b])%7] #일수를 7로 나눈 나머지를 요일 리스트에서 반환
    return answer

#sol2
from datetime import datetime
def solution(a, b): #월, 일
    wd=["MON","TUE","WED","THU","FRI","SAT","SUN"] #요일
    answer=wd[datetime(2016,a,b).weekday()]
    return answer

'''
#sol1
평균 실행 시간 : 0.0 평균 메모리 사용량: 10.157
#sol2
평균 실행 시간 : 0.003 평균 메모리 사용량: 10.121

처음에 짤 때 datetime 안 쓰고 짜는 것을 목표로 해서 달력 보고 요일 순서 맞추는,, 아주 사소한 노력이 들어갔다
datetime 쓰고 짜니까 너무 편하고 쉬웠다...
그런데 sol1이 생각보다 더 빠르게 나와서 조금 놀랐다,,
'''