#sol1
def solution(dartResult): #점수|보너스|[옵션]으로 이루어진 문자열 3세트
    bonus={"S":1,"D":2,"T":3} #보너스 영역
    point=[]
    idx=0
    for i,item in enumerate(dartResult):
        if item.isalpha(): #영역
            point+=[int(dartResult[idx:i])**bonus[item]] #슬라이싱으로 점수 가져와서 포인트 계산
            idx=i+1
        elif not item.isnumeric(): #옵션
            idx=i+1
            if item=="#":
                point[-1]*=-1 #옵션은 해당 세트의 포인트가 리스트에 추가된 후이므로 -1로 접근
            else:
                point[-2:]=[p*2 for p in point[-2:]]
    return sum(point)

#sol2
def solution(dartResult): #점수|보너스|[옵션]으로 이루어진 문자열 3세트
    bonus={"S":1,"D":2,"T":3} #보너스 영역
    point=[]
    tmp=""
    p=0
    for i in dartResult:
        if i.isnumeric(): #점수
            if not tmp:
                point+=[p] #지난 세트 포인트
            tmp+=i #10 대응
        elif i.isalpha(): #영역
            p=int(tmp)**bonus[i] #점수 계산
            tmp=""
        else:
            if i=="#": #옵션
                p*=-1
            else:
                p*=2
                point[-1:]=[j*2 for j in point[-1:]]
    return sum(point)+p #추가되지 않은 포인트 합산

'''
#sol1
평균 실행 시간 : 0.029 평균 메모리 사용량: 10.381
#sol2
평균 실행 시간 : 0.027 평균 메모리 사용량: 10.3

로직이 미묘하게 다른듯 같은데 실행 시간도 거의 같아서 좀 재밌었다
둘 중 하나를 고른다면 sol1을 쓸 것 같다
'''