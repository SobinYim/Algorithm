#sol
import datetime
for t in range(int(input())):
    m,d=map(int,input().split()) #월, 일
    print(f"#{t+1}",datetime.datetime(2016,m,d).weekday())

#sol2
dd=[31,29,31,30,31,30,31,31,30,31,30] #윤년이므로 2번째 요소는 29
for t in range(int(input())):
    m,d=map(int,input().split()) #월, 일
    print(f"#{t+1}",(sum(dd[:(m-1)])+d+3)%7) #2016년에서 지나간 날짜 + 3 (월요일:0~일요일:6의 형식을 맞추기 위함) % 7

'''
sol은 datetime의 weekday 메서드를 이용하여 요일을 구하였고, sol2에서는 날짜에 7을 나누어주는 방식을 사용하였음

제출일 기준 python 코드길이 4위
'''