#sol
def solution(wallpaper): #컴퓨터 바탕화면 문자열 배열
    start,end,y=[],[],[] #가장 왼쪽 파일 위치, 가장 오른쪽 파일 위치, 파일이 위치한 줄
    for idx,i in enumerate(wallpaper):
        if (loc_start:=i.find("#"))!=-1: #해당 줄에 파일이 있다면
            start.append(loc_start)
            end.append(i.rfind("#"))
            y.append(idx)
    return [min(y),min(start),max(y)+1,max(end)+1]

#sol1
import re
def solution(wallpaper): #컴퓨터 바탕화면 문자열 배열
    start,end,y=[],[],[] #가장 왼쪽 파일 위치, 가장 오른쪽 파일 위치, 파일이 위치한 줄
    for idx,i in enumerate(wallpaper):
        res=re.search("#.+#|##|#",i) #해당 줄에 파일이 있다면
        if res:
            start.append(res.start())
            end.append(res.end())
            y.append(idx)
    return [min(y),min(start),max(y)+1,max(end)]

#sol2
def solution(wallpaper): #컴퓨터 바탕화면 문자열 배열
    luy,lux,rdy,rdx=-1,len(wallpaper[0]),-1,-1 #초기화
    for idx,i in enumerate(wallpaper):
        if (loc_start:=i.find("#"))!=-1: #해당 줄에 파일이 있다면
            rdy=idx
            if luy==-1:
                luy=idx
            if loc_start<lux:
                lux=loc_start
            if rdx<=(loc_end:=i.rfind("#")):
                rdx=loc_end
    return [luy,lux,rdy+1,rdx+1]

'''
sol
평균 실행 시간 : 0.016 평균 메모리 사용량: 10.164
sol1
평균 실행 시간 : 0.127 평균 메모리 사용량: 10.19
sol2
평균 실행 시간 : 0.01 평균 메모리 사용량: 10.255

sol,sol1은 파일의 위치 #을 찾을 때 사용하는 함수만 다르고 같은 풀이
시작 위치와 끝 위치, 파일이 있는 y축을 리스트에 담아서 마지막에 min/max로 한 번에 반환한다
re와 str.find를 써봤는데 find 쪽이 훨씬 빨랐다
re는 "#.+#|##|#"로 범위를 좁히며 찾았고 span,start,end 메서드가 있어서 편했다
특히 end를 쓰면 1을 더해주지 않아도 된다!
sol2는 순회마다 값을 비교하여 점 S에서는 작은 값을, 점 E에서는 큰 값을 취한다
좀 의아했던 건 다른 사람의 풀이에서 luy,rdy 값도 비교하는 코드가 많았는데 y를 저장할 때는 min/max 비교를 하지 않아도 된다..!
(당연히) 가장 먼저 나온 값이 최솟값이고 가장 나중에 나온 게 최댓값이니까...!
'''