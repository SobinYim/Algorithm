#sol : 정렬
ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    sq=list(map(int,input().split())) #직사각형의 세 변의 길이
    sq=sorted(sq,key=lambda x: sq.count(x))
    ans.append(f"#{t} {sq[0]}")
for a in ans:
    print(a)

#sol2 : set
ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    sq=list(map(int,input().split())) #직사각형의 세 변의 길이
    res=abs(sum(set(sq))*2-sum(sq))
    ans.append(f"#{t} {res}")
for a in ans:
    print(a)

'''
직사각형 변의 길이의 합은 2x+2y이므로

sol에서는 
빈도 순으로 오름차순 정렬 후, 0번째 요소를 취하여 짝이 맞지 않는 변을 출력함

sol2에서는
set를 이용하여 중복 값을 제거한 값에 2를 곱한 것과 세 변의 합의 차를 구하였음 
정사각형의 경우 모든 변이 같은 길이이므로 절댓값을 취하였음

제출일 기준 python 실행시간 12위(sol2)
'''