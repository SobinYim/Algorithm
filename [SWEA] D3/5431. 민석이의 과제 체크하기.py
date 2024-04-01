#sol
T=int(input()) #tc 개수
for t in range(1,T+1):
    tot,n=map(int,input().split()) #수강생의 수, 과제를 제출한 사람의 수
    li=list(map(int,input().split())) #과제를 제출한 사람의 번호
    res=[i for i in range(1, tot+1) if i not in li] #수강생의 번호 중, 과제를 제출한 번호 리스트에 없을 경우 res 리스트에 추가
    print(f"#{t}", *res)

#sol2
ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    tot,n=map(int,input().split()) #수강생의 수, 과제를 제출한 사람의 수
    s=set(map(int,input().split())) #과제를 제출한 사람의 번호
    res=set(range(1,tot+1))-s #수강생의 번호 집합에서 과제를 제출한 사람의 번호 집합을 차집합
    ans.append(f"#{t} {' '.join(map(str,res))}") #f string 에서는 *언패킹 사용이 불가능해서 join을 통해 이어주었음
for a in ans:
    print(a)

'''
sol은 for문과 if문을 이용하였고, sol2는 차집합을 이용하였음

제출일 기준 python 코드길이 2위, 실행시간 13위(sol2)
'''