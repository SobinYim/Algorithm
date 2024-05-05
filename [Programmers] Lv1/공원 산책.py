#sol
class Walk:
    def __init__(self,park): #공원
        self.x,self.y=0,0
        self.park=park
        self.h,self.w=len(self.park),len(self.park[0])
    def find_starting_point(self): #시작 지점 탐색
        for idx,m in enumerate(self.park):
            self.park[idx]=list(m)
            if (s:=m.find("S"))!=-1: #"S"를 찾으면 x,y를 지정하고 break
                self.x,self.y=s,idx
                break
    def cal_destination(self,op,n): #도착 지점 계산(없으면 -1 반환)
        if op in ["N","S"]: #세로축 이동
            destination=self.y+n
            if 0<=destination<self.h: #범위 안이라면
                return destination
        else:
            destination=self.x+n
            if 0<=destination<self.w: #범위 안이라면
                return destination
        return -1
    def valid_route(self,op,destination): #경로 검사(경로에 장애물이 있다면 False, 없다면 True 반환)
        if op=="N":
            for i in range(destination,self.y):
                if self.park[i][self.x]=="X":
                    return False
        elif op=="S":
            for i in range(self.y+1,destination+1):
                if self.park[i][self.x]=="X":
                    return False
        elif op=="E":
            if "X" in self.park[self.y][self.x:destination+1]:
                return False
        else:
            if "X" in self.park[self.y][destination:self.x]:
                return False
        return True

def solution(park, routes): #공원을 나타내는 문자열 배열, 수행할 명령
    walk=Walk(park)
    walk.find_starting_point()
    for i in routes:
        op,n=i.split() #방향, 거리
        n=int(n) if op in ["S","E"] else -int(n)
        if (destination:=walk.cal_destination(op,n))!=-1 and walk.valid_route(op,destination): #도착 지점이 존재하고 경로에 장애물이 없다면
            if op in ["N","S"]:
                walk.y=destination
            else:
                walk.x=destination
    return [walk.y,walk.x]

#sol2
def solution(park, routes): #공원을 나타내는 문자열 배열, 수행할 명령
    for idx,m in enumerate(park): #시작 지점 탐색
        park[idx]=list(m)
        if (s:=m.find("S"))!=-1:
            x,y=[s,idx]
            break
    h,w=len(park),len(park[0]) #높이, 폭
    for r in routes:
        op,n=r.split() #방향, 거리
        n=int(n)
        if op=="N": #북쪽으로 이동
            if y-n<0: #도착 지점이 유효한지
                continue
            for i in range(y-n,y): #경로가 유효한지
                if park[i][x]=="X":
                    break
            else:
                y-=n
        elif op=="S": #남쪽으로 이동
            if h<=y+n:
                continue
            for i in range(y+1,y+n+1):
                if park[i][x]=="X":
                    break
            else:
                y+=n
        elif op=="E": #동쪽으로 이동
            if w<=x+n:
                continue
            if "X" not in park[y][x+1:x+n+1]:
                x+=n
        else: #서쪽으로 이동
            if x-n<0:
                continue
            if "X" not in park[y][x-n:x]:
                x-=n
    return [y,x]

'''
sol
평균 실행 시간 : 0.09 평균 메모리 사용량: 10.44
sol2
평균 실행 시간 : 0.07 평균 메모리 사용량: 10.43

sol1과 sol2는 일단 토대가 같다
sol2 방식으로 짜다가 보기 힘들어서 분리를 해볼까 하다 class를 이용하는 방향으로 틀었다
class를 이용해서 sol2는 방향마다 동작을 지정한 반면
sol1에서는 묶을 수 있는 부분은 묶어서 처리했다
N/S 방향의 경우 컴프리헨션을 이용하지 않고 for문으로 경로를 탐색하다 장애물이 나오면 멈추고 다음 route를 찾았다
아마 그래서 다른 풀이에 비해 좀 빠르지 않나 싶다

대신에 다른 사람의 풀이는 조금 더 포괄적으로 동작하는 게 장점인 것 같다
x,y에 n에 0이나 -1/1를 곱해서 도착 지점 계산하는 발상 좋았다
min/max로 range 지정하는 코드 보고 감탄했다
min(xy,destination), max(xy+1,destination+1) 하면 NS/EW를 또 묶을 수 있게 된다! 굿
'''