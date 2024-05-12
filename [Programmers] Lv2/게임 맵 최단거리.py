#sol
def solution(maps):
    h,w=len(maps)-1,len(maps[0])-1
    op=[(1,0),(-1,0),(0,1),(0,-1)]
    visited=set()
    visit=[(0,0)]
    step=1
    while visit:
        step+=1
        visit_this=set()
        for x,y in visit:
            for a,b in op:
                if 0<=(new_x:=x+a)<=w and 0<=(new_y:=y+b)<=h and maps[new_y][new_x] and (new_x,new_y) not in visited:
                    visit_this.add((new_x,new_y))
                    if (new_x,new_y)==(w,h):
                        return step
        visited.update(visit)
        visit=visit_this
    return -1

#sol1
def solution(maps):
    h,w=len(maps)-1,len(maps[0])-1
    op=[(1,0),(-1,0),(0,1),(0,-1)]
    visited=set()
    visit=[(0,0)]
    step=1
    while visit:
        step+=1
        visit_this=set()
        for x,y in visit:
            for a,b in op:
                if not a and 0<=(ny:=y+b)<=h:
                    nx=x
                elif not b and 0<=(nx:=x+a)<=w:
                    ny=y
                else:
                    continue
                if maps[ny][nx] and (nx,ny) not in visited:
                    visit_this.add((nx,ny))
                    if nx==w and ny==h:
                        return step
        visited.update(visit)
        visit=visit_this
    return -1

'''
sol
[효율성 테스트] 평균 실행 시간 : 8.22 평균 메모리 사용량: 10.77
sol1
[효율성 테스트] 평균 실행 시간 : 6.68 평균 메모리 사용량: 10.8

sol과 sol1은 같은 풀이다
조건을 수정해서 불필요한 연산을 줄였다
생각보다 차이가 크게 나서 좀 놀라웠다

인상 깊었던 다른 사람의 풀이:
def solution(maps):
    mp = [[-1]*(len(maps[0]) + 2)]
    for r in maps:
        row = list(map(lambda x: x-1, r))
        row.insert(0, -1)
        row.append(-1)
        mp.append(row)
    mp.append([-1] * (len(maps[0]) + 2))
    mp[1][1] = 1
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    dst = (len(maps), len(maps[0]))
    q = [(1, 1)]
    while q:
        f = q.pop(0)
        if f == dst:
            return mp[f[0]][f[1]]
        for d in directions:
            ny = f[0] + d[0]
            nx = f[1] + d[1]
            if mp[ny][nx] == 0:
                mp[ny][nx] = mp[f[0]][f[1]] + 1
                q.append((ny, nx))
    return -1
[효율성 테스트] 평균 실행 시간 : 5.63 평균 메모리 사용량: 10.27
보통 실행 시간이 짧은 풀이들은 조건문으로 방향마다 동작을 지정해서 코드가 40-50줄 정도로 꽤 길었는데
이 풀이는 비교적 짧고 심플한 코드인데도 실행 시간이 굉장히 잘 나왔다
요약하자면 maps에 패딩을 추가한 mp를 사용하여 인덱스 에러를 방지하고, if문 연산을 줄여 시간을 단축한다
패딩 생각은 미처 못했는데 아주 좋은 방법 같다! 
'''