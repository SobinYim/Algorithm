T=int(input()) #tc 개수
for t in range(1,T+1):
    d,h,m=map(lambda x: int(x)-11,input().split()) #약속 시간이 11-11 11:11이므로 일, 시각, 분에 각각 11씩을 감하여 줌
    if d<0 or (d==0 and h<0) or (d==h==0 and m<0): #약속 시간 이전에 차였을 경우
        m=-1
    else: #분 단위로 계산
        h+=d*24
        m+=h*60
    print(f"#{t}",m)