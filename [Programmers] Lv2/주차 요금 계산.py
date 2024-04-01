#sol1
from math import ceil
def cal_time(t): #hh:mm형식으로 주어진 시간 데이터를 분 단위로 환산하여 반환
    hh,mm=map(int,t.split(":"))
    return hh*60+mm

def solution(fees, records): #요금표, 입/출차 기록
    reg_number_dict=dict() #차량 번호:[누적 시간, 출차 시간] 딕셔너리
    for i in records[::-1]:
        t,rn,b=i.split() #시간, 차량 번호, 내역
        if b=="IN":
            if rn not in reg_number_dict.keys(): #입차인데 차량 번호가 기록에 없으면(==출차하지 않음)
                reg_number_dict[rn]=[0,1439]
            reg_number_dict[rn][0]+=reg_number_dict[rn][1]-cal_time(t) #누적 시간 업데이트
        else:
            if rn in reg_number_dict.keys():
                reg_number_dict[rn][1]=cal_time(t) #출차 시간 업데이트
            else:
                reg_number_dict[rn]=[0,cal_time(t)]
    ans=[]
    for i in sorted(reg_number_dict.items()): #차량 번호 순서대로 주차 요금 계산
        fee=ceil(tmp/fees[2])*fees[3] if (tmp:=i[1][0]-fees[0])>=0 else 0
        ans.append(fee+fees[1])
    return ans

#sol2
from math import ceil
def cal_time(t): #hh:mm형식으로 주어진 시간 데이터를 분 단위로 환산하여 반환
    hh,mm=map(int,t.split(":"))
    return hh*60+mm

def solution(fees, records): #요금표, 입/출차 기록
    acc_t=[0]*10000 #누적 시간
    out_t=[0]*10000 #출차 시간
    for i in records[::-1]:
        t,rn,b=i.split() #시간, 차량 번호, 내역
        rn=int(rn)
        if b=="IN":
            if not out_t[rn]: #입차이고 출차 기록이 없으면
                out_t[rn]=1439
            acc_t[rn]+=out_t[rn]-cal_time(t) #누적 시간 업데이트
        else:
            out_t[rn]=cal_time(t) #출차 시간 업데이트
    return [max(ceil((i-fees[0])/fees[2])*fees[3],0)+fees[1] for i in acc_t if i] #주차 요금 계산

'''
#sol1
평균 실행 시간 : 0.6 평균 메모리 사용량: 10.34
#sol2
평균 실행 시간 : 0.78 평균 메모리 사용량: 10.46

sol1과 sol2는 같은 내용
sol2를 짤 때 접근 방식은 같되 좀 짧게 작성하려고 했다
sol1은 딕셔너리로 차량별로 출차, 누적 시간을 저장했고, sol2는 출차, 누적 시간을 따로 리스트로 두었다
또 sol1은 주차 요금 계산에서 if문을 사용했고, sol2는 max를 사용했다
sol2는 차량 번호가 곧 인덱스라 정렬할 필요가 없는 게 장점이고, 사용하지 않은 번호들도 순회를 하게 된다는 건 단점이다
'''