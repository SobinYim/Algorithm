#sol1
def cal_expire_date(date,term): #날짜, 유효 기간
    y,m,d=map(int,date.split("."))
    return y*336+(m+term)*28+d
def solution(today, terms, privacies): #기준일, 약관 정보
    today=cal_expire_date(today,0)
    terms_dict=dict() #약관 종류:유효 기간 딕셔너리
    for i in terms:
        c,t=i.split() #약관 종류, 유효 기간
        terms_dict[c]=int(t)
    ans=[]
    for idx,i in enumerate(privacies):
        d,t=i.split() #날짜, 약관 종류
        if cal_expire_date(d,terms_dict[t])<=today:
            ans.append(idx+1)
    return ans

#sol2
from datetime import date
def solution(today, terms, privacies): #기준일, 약관 정보
    today=date(*map(int,today.split(".")))
    terms_dict=dict() #약관 종류:유효 기간 딕셔너리
    for i in terms:
        c,t=i.split() #약관 종류, 유효 기간
        terms_dict[c]=int(t)
    ans=[]
    for idx,i in enumerate(privacies):
        d,t=i.split() #날짜, 약관 종류
        y,m,d=map(int,d.split("."))
        if (m:=m+terms_dict[t]-1)>=12:
            y+=m//12
            m=m%12
        if date(y,m+1,d)<=today:
            ans.append(idx+1)
    return ans

'''
sol1
평균 실행 시간 : 0.08 평균 메모리 사용량: 10.28
sol2
평균 실행 시간 : 0.09 평균 메모리 사용량: 10.4

sol1>sol2 순으로 짰고 성능 면에서는 sol1이 더 좋기는 하지만 차이가 크지는 않다
sol1은 y*336+month*28+d로 일수로 형식을 맞췄고
sol2는 datetime의 date를 이용해 형식을 맞췄다
m+terms_dict[t]-1은 저 -1이 없으면... month가 0이 되는 참사가 일어날 수 있다(경험담)

다른 사람의 풀이에서 본 코드:
{v[0]: int(v[2:]) * 28 for v in terms}
슬라이싱으로 컴프리헨션 이용+dictionary에 일수를 넣어 계산 과정 간편화
이런 디테일들이 중요한 것 같다..
굿!
'''