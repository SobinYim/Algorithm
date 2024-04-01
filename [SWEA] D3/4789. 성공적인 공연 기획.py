#sol
T=int(input()) #tc 개수
for t in range(1,T+1):
    s=list(map(int,input())) #기립 박수를 치는 관객의 리스트
    acc,res=0,0 #누적합, 고용해야 할 사람의 수
    for i,j in enumerate(s):
        if acc<=i and j==0: #누적 합이 해당 회차의 index보다 크지 않고, 해당 회차에 박수를 치는 사람이 없을 경우(==연쇄가 끊겼을 경우) res에 1을 더함
            res+=1
            acc+=1
        else:
            acc+=j
    print(f"#{t}",res)

#sol2
from itertools import accumulate
T=int(input()) #tc 개수
for t in range(1,T+1):
    s=accumulate(map(int,"0"+input())) #기립 박수를 치는 관객의 누적 합 리스트
    res=0
    for i,j in enumerate(s): #해당 회차의 index와 누적 합+고용한 사람을 비교하여 index가 더 클 경우 res에 1을 더함
        if (j+res)<i:
            res+=1
    print(f"#{t}",res)

'''
제출일 기준 python 코드길이 8위
'''