wkd=["SAT","FRI","THU","WED","TUE","MON","SUN"] #요일
for t in range(int(input())):
    print(f"#{t+1}",wkd.index(input())+1) #요일 리스트에서 입력된 요일을 찾아서 +1

'''
제출일 기준 python 코드길이 2위, 메모리 4위
'''