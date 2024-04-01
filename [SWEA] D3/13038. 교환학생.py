ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    n=int(input())-1 #교환학생으로 들어야 하는 수업 일수
    d=list(input().replace(" ","")) #요일별 교환학생을 위한 수업 유무
    temp=[0]*7 #삼성대학교에서 지내야하는 일수 리스트
    for j in range(7): #수업 시작 일자가 무슨 요일인지에 따라 삼성대학교에서 지내야하는 일자 수
        li=[i for i in range(7) if d[i]=="1"]
        temp[j]=(n//d.count("1"))*7+li[n%d.count("1")]+1
        d.append(d.pop(0))
    res=min(temp) #가장 적은 것을 저장
    ans.append(f"#{t} {res}")
for a in ans:
    print(a)

'''
제출일 기준 python 코드길이 6위
157 ms
'''