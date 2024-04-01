def cal_dist(left_loc,right_loc,key_loc): #왼손 위치, 오른손 위치, 키 위치 > 손과 키가 가까운 방향 반환
    lx,ly=left_loc
    rx,ry=right_loc
    kx,ky=key_loc
    l_dist=abs(kx-lx)+abs(ky-ly) #맨해튼 거리
    r_dist=abs(kx-rx)+abs(ky-ry)
    if l_dist<r_dist:
        return "left"
    elif r_dist<l_dist:
        return "right"
    else:
        return False

def solution(numbers, hand): #눌러야 할 번호, 기본 사용 손
    key=list(range(1,10))+["*",0,"#"]
    coord=[(j,i) for i in range(3,-1,-1) for j in range(3)]
    loc=dict((k,c) for k,c in zip(key,coord)) #키:좌표 딕셔너리
    l,r=loc["*"],loc["#"] #star, sharp
    hand=hand[0],
    ans=""
    for i in numbers:
        key_loc=loc[i]
        if i in [2,5,8,0]: #중앙키
            a=cal_dist(l,r,key_loc)
            if not a: #양 방향 거리가 같을 때
                a=hand
        elif i in [1,4,7]:
            a="left"
        else:
            a="right"
        if a=="left": #왼손 타이핑
            ans+="L"
            l=key_loc
        else: #오른손 타이핑
            ans+="R"
            r=key_loc
    return ans

'''
평균 실행 시간 : 0.11 평균 메모리 사용량: 10.29

어렵진 않았는데 좀 더 깔끔하게 못 짜서 아쉬운 코드,,
ans+= 부분을 if 바깥에서 처리하거나 cal_dist에 매개 변수로 전달해서 아예 방향만 반환하도록 짜보기도 했는데 생각이랑 다르게 실행 시간이 늘었다
왜인지 잘 모르겠다.. 그냥 오차인가 싶기도 하다...
'''