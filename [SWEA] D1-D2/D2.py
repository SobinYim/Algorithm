'''
1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기
'''
T=int(input()) #tc 개수
for t in range(T):
    n=int(input()) #tc 번호
    sc=list(map(int,input().rstrip().split())) #점수
    res=sorted(sc,key=lambda x: sc.count(x),reverse=True)[0] #빈도순으로 정렬 후, 가장 첫 번째로 오는 수 반환(정렬 후 내림차순으로 정렬되기 때문에 reverse 옵션 이용)
    print(f"#{n}",res)


'''
1284. 수도 요금 경쟁
'''
T=int(input()) #tc 개수
for i in range(1, T+1):
    P,Q,R,S,W=map(int,input().split())
    a=W*P
    b=(W-R)*S+Q if W>R else Q
    print(f"#{i}",min(a,b))


'''
1288. 새로운 불면증 치료법
'''
T = int(input()) #tc 개수
for i in range(1,T+1):
    sn=input() #첫번째 수(str)
    n=int(sn) #첫번째 수(int)
    n_set=set() #빈 집합
    cnt=1 #양을 센 횟수
    while True: #집합 요소가 10개(0~9)가 될 때까지 배수를 만들고 집합에 각 자릿수를 넣는 것을 반복
        n_set=n_set.union(sn)
        if len(n_set)==10:
            break
        else:
            cnt+=1
            sn=str(cnt*n)
    print(f"#{i}",sn)


'''
1940. 가랏! RC카!
'''
T=int(input()) #tc 개수
for t in range(1,T+1):
    n=int(input()) #커맨드의 개수
    d,s=0,0 #rc카의 위치와 속도 초기화
    for i in range(n):
        c=input().split() #커맨드(0 : 현재 속도 유지, 1 : 가속, 2 : 감속)
        ac=int(c[1]) if len(c)>1 else 0 #가속도의 값
        c=int(c[0])
        if c==1:
            s+=ac
        elif c==2:
            s=s-ac if s-ac>=0 else 0
        d+=s
    print(f"#{t}",d)


'''
1945. 간단한 소인수분해
'''
T=int(input()) #tc 개수
numbers=[2, 3, 5, 7, 11]
for t in range(1, T+1):
    res=[]
    n = int(input()) #소인수 분해할 숫자
    for number in numbers:
        cnt = 0 #cnt 초기화
        while True: #해당 숫자로 더 이상 나누어지지 않을 때까지 반복
            if n % number == 0:
                n = n // number
                cnt += 1
            else:
                res.append(str(cnt))
                break
    print('#{} {}'.format(t, ' '.join(res)))


'''
1946. 간단한 압축 풀기
'''
T=int(input()) #tc 개수
for t in range(1,T+1):
    n=int(input()) #알파벳-숫자 쌍의 개수
    res="" #res 빈 문자열로 초기화
    for i in range(n):
        a,an=input().split() #알파벳과 알파벳 개수
        res+=a*int(an) #문서 압축 해제
    print(f"#{t}")
    for i in range(len(res)//10+1): #10개씩 출력
        print(res[i*10:(i+1)*10])


'''
1948. 날짜 계산기
'''
T = int(input()) #tc 개수
d_li = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #월별 날짜 리스트
for t in range(1,T+1):
    m1,d1,m2,d2=map(int,input().split())
    res=sum(d_li[m1:m2])+d2-d1+1
    print(f"#{t}",res)


'''
1959. 두 개의 숫자열
'''
def put(): #반복 사용할 input 함수 정의
    return map(int,input().split())
def max_fn(li_long,li_short):
    d=len(li_long)-len(li_short) #긴 리스트와 짧은 리스트의 길이 차이
    li_short=[0]*(d)+li_short #길이 차이만큼 짧은 리스트에 0을 넣어줌
    li_res=[] #결과 저장할 리스트
    for k in range(d+1): #각 자릿수의 곱의 합을 구한 후, 맨 앞의 0을 지우고 뒤에 추가하여 짧은 리스트를 이동
        li_res.append(sum([li_long[j]*li_short[j] for j in range(len(li_short))]))
        li_short.pop(0)
        li_short.append(0)
    return max(li_res) #결과 리스트의 최댓값 반환

t=int(input()) #tc 개수
for i in range(1,t+1):
    len_a,len_b=put()
    li_a=list(put())
    li_b=list(put())
    if len_a>len_b:
        res=max_fn(li_a,li_b)
    else:
        res=max_fn(li_b,li_a)
    print(f"#{i}",res)


'''
1961. 숫자 배열 회전
'''
def fn_r(n,li_org): #90도 회전 함수
    li=list(li_org)
    li.reverse()
    li_t=[]
    for i in range(n):
        tg=""
        for j in range(n):
            tg+=li[j][i]
        li_t.append(tg)
    return li_t

T = int(input()) #tc 개수
for t in range(1,T+1):
    n=int(input())
    li=[]
    for i in range(n):
        li.append(input().replace(" ",""))
    li_90=fn_r(n,li)
    li_180=fn_r(n,li_90)
    li_270=fn_r(n,li_180)
    print(f"#{t}")
    for i in range(n):
        print(li_90[i],li_180[i],li_270[i])


'''
1966. 숫자를 정렬하자
'''
T = int(input()) #tc 개수
for t in range(1,T+1):
    _=input()
    li=sorted(map(int,input().split())) #split한 문자를 숫자로 바꾼 후 정렬
    print(f"#{t}"," ".join(map(str,li)))


'''
1970. 쉬운 거스름돈
'''
T=int(input()) #tc 개수
for t in range(1,T+1):
    money = {50000: 0, 10000: 0, 5000: 0, 1000: 0, 500: 0, 100: 0, 50: 0, 10: 0}  #화폐 단위-개수 쌍
    n=int(input()) #거슬러주어야 할 금액
    for i in money: #n을 화폐 단위 i로 나누고 값을 dict에 저장, n은 i로 나눈 나머지로 저장
        money[i]=n//i
        n%=i
    print(f"#{t}")
    for i in money.values():
        print(i,end=" ")
    print()


'''
1974. 스도쿠 검증
'''
T=int(input()) #tc 개수
for t in range(1,T+1):
    res=1
    li=[list(map(int,input().split(" "))) for j in range(9)] #스도쿠 판 받기
    for i in range(len(li)):
        set_h=set(li[i]) #세로줄
        set_v=set() #가로줄 초기화
        for j in range(len(li)):
            set_v.add(li[j][i]) #가로줄
            if i%3==0 and j%3==0: #3*3 정사각형 공간 시작점 마다
                set_z=set() #정사각형 초기화
                if len(set_z.union(li[j][i:i+3],li[j+1][i:i+3],li[j+2][i:i+3]))!=9: #정사각형 검증
                    res=0
                    break
        if res==0 or len(set(li[i]))+len(set_v)!=18: #res가 이미 0인 경우이거나 세로/가로줄 검증하여 불가능하면
            res=0
            break
    print(f"#{t}",res)


'''
1976. 시각 덧셈
'''
T=int(input()) #tc 개수
for t in range(1,T+1):
    h1,m1,h2,m2=map(int,input().split()) #시각
    m=m1+m2 #분 덧셈
    m,h=(m,0) if m<60 else (m-60,1) #60 초과분 빼고 시각에 더해줌
    h+=h1+h2 #시각 덧셈
    h=h if h<12 else h-24 if h>24 else h-12 #시각 12진법으로 표기
    print(f"#{t}",h,m)


'''
1979. 어디에 단어가 들어갈 수 있을까
'''
T = int(input()) #tc 개수
for t in range(1,T+1):
    n,w=map(int,input().split()) #퍼즐 크기와 단어 길이 받기
    li = []
    count = 0 #들어갈 수 있는 횟수
    for i in range(n):
        tg=input().replace(" ","") #입력받은 후, 불필요한 공백 제거
        li.append(tg) #list에 추가
        count += tg.split("0").count("1"*w) #단어가 들어갈 수 없는 0을 기준으로 문자열을 나눈 후, 단어의 길이만큼 공간이 있는 칸을 찾음
    for j in range(len(li)): #돌려서 같은 작업 반복
        tg = ""
        for k in range(len(li)):
            tg += li[k][j]
        count += tg.split("0").count("1"*w)
    print(f"#{t}", count)


'''
1983. 조교의 성적 매기기
'''
T=int(input()) #tc 개수
sc_d=["A+","A0","A-","B+","B0","B-","C+","C0","C-","D0"]
for t in range(1,T+1):
    n,tg=map(int,input().split()) #학생 수와 학생 번호 입력
    sc_li=[] #학생들의 점수 리스트
    for i in range(n):
        me,fe,hw=map(int,input().rstrip().split()) #중간, 기말, 과제 점수 입력
        sc=me*0.35+fe*0.45+hw*0.2 #최종 점수 계산
        sc_li.append(sc)
        if i==tg-1: #학생 점수 저장
            tg_sc=sc
    sc_li=sorted(sc_li,reverse=True) #점수 순으로 정렬 후, 학생 점수로 순위 계산
    idx=sc_li.index(tg_sc)
    idx=int(idx//(n/10)) #학생의 백분위 단위
    print(f"#{t}",sc_d[idx])


'''
1984. 중간 평균값 구하기
'''
T=int(input()) #tc 개수
for t in range(1,T+1):
    li=sorted(map(int,input().rstrip().split()))[1:-1] #입력받은 수의 최소/최대 수를 제외하고 저장
    print(f"#{t}",round(sum(li)/len(li)))


'''
1986. 지그재그 숫자
'''
T = int(input()) #tc 개수
for i in range(1, T + 1):
    num=int(input())
    res=sum([i if i%2==1 else -i for i in range(num+1)])
    print(f"#{i}",res)

#sol2 : 문제에서는 n이 작아서 크게 상관 없으나 n이 커지면 성능이 저하되므로 계산으로 구현
from math import ceil
T = int(input()) #tc 개수
for i in range(1, T + 1):
    num=int(input())
    cal=ceil(num/2)
    res=-cal if num%2==0 else cal
    print(f"#{i}",res)


'''
1989. 초심자의 회문 검사
'''
T = int(input()) #tc 개수
for i in range(1, T + 1):
    s=input()
    res=1 if s==s[::-1] else 0
    print(f"#{i}",res)


'''
2001. 파리 퇴치
'''
T=int(input()) #tc 개수
for t in range(1, T+1):
    n,s=map(int, input().split()) #필드의 크기와 파리채 크기
    li=[list(map(int,input().split())) for _ in range(n)]
    res=[]
    for c in range(n-s+1): #열
        for r in range(n-s+1): #행
            temp=0 #파리
            for i in range(s):
                temp+=sum(li[i+r][c:c+s])
            res.append(temp)
    print(f"#{t}",max(res))


'''
2005. 파스칼의 삼각형
'''
T=int(input()) #tc 개수
for t in range(1,T+1):
    n=int(input()) #삼각형의 층
    print(f"#{t}")
    li=[0, 1]
    for i in range(n): #앞 뒤에 0을 추가한 리스트(li)의 두 요소씩 더하고, 이 결과값의 리스트(t_li)를 li에 다시 저장
        t_li=[0]
        for j in range(len(li) - 1):
            print(li[j]+li[j+1],end=" ")
            t_li.append(li[j]+li[j+1])
        t_li.append(0)
        li=list(t_li)
        print()


'''
2007. 패턴 마디의 길이
'''
T = int(input()) #tc 개수
for t in range(1,T+1):
    s = input() #문자열
    for i in range(1,len(s)): #마디의 길이 i++
        if s[:i]==s[i:i+i]: #i의 길이를 가진 두 문자열이 같으면
            res=s[:i]
            if len(s)//len(res)==s.count(res): #전체 문자열에서 마디의 길이 i를 나눈 몫이 전체 문자열에서 마디를 count한 수와 같으면 break
                break
    print(f"#{t}",len(res))


'''
1926. 간단한 369게임
'''
for i in range(1,int(input())+1): #정수 n까지
    t=str(i) #현재 숫자 i
    r=t.count("3")+t.count("6")+t.count("9")
    print(t if r==0 else "-"*r, end=" ") #3 or 6 or 9의 개수만큼 -로 바꾸어 줌


'''
1859. 백만 장자 프로젝트
'''
T=int(input()) #tc 개수
for t in range(1,T+1):
    d=int(input()) #원재가 매매가를 알고있는 날짜 수
    p=list(map(int,input().rstrip().split())) #매매가
    res=0 #이윤
    temp=0 #원재가 구매한 물건의 개수
    mx=p.index(max(p)) #최고가 일자
    for i in range(d):
        if i<mx: #최고가 이전까지는 모두 구매
            temp+=1
            res-=p[i]
        else:
            res+=temp*p[i] #판매
            if mx!=len(p)-1:
                mx+=p[mx+1:].index(max(p[mx+1:]))+1 #그 다음으로 높은 가격으로 갱신
            temp=0
    print(f"#{t}",res)