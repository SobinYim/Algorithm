#sol : for문으로 모든 경우의 수
def chn(nli,li): #nli의 두 인덱스 li를 서로 바꾸어 정수 변환 후 반환, 문자 0으로 시작할 경우, -1 반환
    dg,tg=li
    n=nli.copy()
    n[dg],n[tg]=n[tg],n[dg]
    if n[0]=="0":
        return -1
    else:
        return int("".join(n))
ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    n=input() #정수
    nli=list(n) #n을 list 변환
    li=[] #인덱스의 조합
    for i in range(len(n)): #인덱스 두 개 선택
        for j in range(i+1,len(n)):
            li.append((i,j))
    res=list(filter(lambda x: x>0,(map(lambda x: chn(nli,x),li))))+[int(n)] #두 인덱스의 위치를 바꾸고, -1 값 제거, 인덱스를 바꾸지 않은 n을 리스트에 함께 넣어 줌
    maxn,minn=max(res),min(res) #최댓값과 최소값
    ans.append(f"#{t} {minn} {maxn}")
for a in ans:
    print(a)

#sol2
def chn(nli,li): #nli의 두 인덱스 li를 서로 바꾸어 문자열 변환 후 반환, 빈 튜플일 경우 에러가 나므로 try-except문으로 예외 처리
    n=nli.copy()
    try:
        dg,tg=li
        n[dg],n[tg]=n[tg],n[dg]
    except:
        pass
    return "".join(map(str,n))
ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    n=list(map(int,input().rstrip())) #각각의 자릿수를 정수 변환한 리스트
    d=sorted(n,reverse=True) #내림차순 정렬(최댓값 탐색)
    d1=d.copy()[::-1] #오름차순 정렬(최솟값 탐색)
    if 0 in n and len(n)>1: #리스트 안에 0이 들어갈 경우 맨 처음 수가 0이 들어올 수 없으므로 이를 처리한 리스트
        d1.insert(0,d1.pop(d1.count(0)))
    xi,ni=(),() #최댓값을 만들기 위한 인덱스, 최솟값 만들기 위한 인덱스
    for i in range(len(n)): #인덱스가 비어있고, 숫자의 i번째 수가 정렬된 리스트의 숫자와 다르면 원래 들어와야 하는 숫자의 위치를 뒤에서부터 탐색, 튜플 형태로 저장
        if xi==() and n[i]!=d[i]:
            xi=((i,-(n[::-1].index(d[i])+1)))
        if ni==() and n[i]!=d1[i]:
            ni=((i,-(n[::-1].index(d1[i])+1)))
        if xi and ni: #두 인덱스 튜플이 비어있지 않다면 break
            break
    maxn,minn=chn(n,xi),chn(n,ni) #최댓값과 최소값
    ans.append(f"#{t} {minn} {maxn}")
for a in ans:
    print(a)

#sol3
def fn(n,d,xn): #수, 정렬된 리스트, 최댓값인지 최솟값인지
    dg,idx=0,0 #서로 바꿀 인덱스 값 초기화
    if d[xn]=="0" and n[0]!=sorted(set(n))[1]: #0이 포함된 수에서 최솟값을 만들기 위한 인덱스 탐색(첫 자릿수를 바꿔야 할 경우)
        tg=sorted(set(n))[1]
        idx=n.rfind(tg)
        return (dg,idx)
    if d[xn]=="0" and n[0]==sorted(set(n))[1]: #0이 포함된 수에서 최솟값을 만들기 위한 인덱스 탐색(첫 자릿수를 바꾸지 않아도 될 경우)
        d.remove(sorted(set(n))[1])
        n=n[1:]
        dg,idx=1,1
        if len(n)==1:
            return (dg,idx)
    try:
        dg+=[i for i in range(len(d)) if n[i]!=d[i]][0] #그 외의 경우(최댓값, 0이 포함되지 않은 최솟값)
    except:
        dg=len(n)-1 #n과 정렬된 리스트가 동일하면 빈 리스트이므로 에러가 나는데 이를 처리하기 위한 except
    tg=d[dg] if idx==0 else d[dg-1]
    idx+=n.rfind(tg)
    return (dg,idx)
def chn(n,li): #n의 두 인덱스 li의 위치를 바꾸어 줌
    dg,tg=li
    n=list(n)
    n[dg],n[tg]=n[tg],n[dg]
    return "".join(n)
ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    n=input().rstrip() #정수
    d=sorted(n,reverse=True) #n의 각 자릿수를 내림차순 정렬
    maxn=n if list(n)==d else chn(n,fn(n,d,1)) #정렬된 리스트와 비교하여 같다면 n을 그대로 쓰고 아니라면 인덱스를 바꿈
    d.reverse() #오름차순 정렬
    minn=n if list(n)==d else chn(n,fn(n,d,0)) #정렬된 리스트와 비교하여 같다면 n을 그대로 쓰고 아니라면 인덱스를 바꿈
    ans.append(f"#{t} {minn} {maxn}")
for a in ans:
    print(a)

'''
sol3(167ms)>sol(129ms)>sol2(107ms) 순으로 짰고
사실 sol3은 몇 개월 전에 짠 코드라 기억이 잘 안 나서 그냥 처음부터 다시 짰다
sol2를 짤 때, 문제 해결 방식에서는 sol3을 계승하되 복잡하지 않고 이해하기 쉽게 만드는 데에 초점을 맞췄다
sol이 개인적으로 뇌가 가장 편해서 마음에 들었다!

제출일 기준 python 실행시간 5위, 메모리 2위(sol2)
'''