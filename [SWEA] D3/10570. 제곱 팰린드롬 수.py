#sol
p=[] #제곱 팰린드롬 수
for i in range(1,1000):
    sq=i**2
    if sq>1000: #제곱한 수가 주어질 수 있는 최댓값을 초과하면 반복 중지
        break
    si,ssq=str(i),str(sq) #회문 판정을 위해 형 변환
    if si==si[::-1] and ssq==ssq[::-1]: #i와 이를 제곱한 값이 회문이면 리스트에 추가
        p.append(sq)

T=int(input()) #tc 개수
for t in range(1,T+1):
    s,e=map(int,input().split()) #시작점과 끝점
    res=0 #결과 값 초기화
    for i in p: #팰린드롬 수가 끝 점을 초과하면 반복 중지, 시작점 이상이면 res에 1을 더함
        if e<i:
            break
        if i>=s:
            res+=1
    print(f"#{t}",res)

#sol2
p=[] #제곱 팰린드롬 수
n,sq=1,1 #초기 숫자와 제곱 값
while sq<1000: #제곱 값이 주어진 수를 초과할 때까지 반복
    sn,ssq=str(n),str(sq) #회문 판정을 위해 형 변환
    if sn==sn[::-1] and ssq==ssq[::-1]:
        p.append(sq) #i와 이를 제곱한 값이 회문이면 리스트에 추가
    n+=1 #n에는 1을 더하고 sq에는 제곱한 값을 할당
    sq=n**2

T=int(input()) #tc 개수
for t in range(1,T+1):
    s,e=map(int,input().split()) #시작점과 끝점
    res=len(list(filter(lambda x: s<=x<=e,p))) #시작점과 끝점 사이의 팰린드롬 수를 filter로 거르고, 이 길이를 res에 할당
    print(f"#{t}",res)

#sol3
def fn_c(x): #회문 확인
    x=str(x)
    if x==x[::-1]:
        return 1
    else:
        return 0
def fn_p(x): #제곱근이 정수형이 아니거라면 0을 반환, 아니라면 제곱근의 회문 판정
    import math
    sqx=0 if math.sqrt(x)%1 !=0 else fn_c(int(math.sqrt(x)))
    return (fn_c(x) and sqx)

T=int(input()) #tc 개수
for t in range(1,T+1):
    s,e=map(int,input().split()) #시작점과 끝점
    res=sum(map(fn_p,range(s,e+1))) #시작점부터 끝점까지 제곱 팰린드롬 확인 후, 합계(개수)
    print(f"#{t}",res)

'''
처음엔(sol3) 함수를 이용해서 그때그때 검사하는 방법을 사용했는데 매번 제곱 팰린드롬 검사를 해주어야 해서 비효율적이라고 판단,
정리하면서 sol, sol2와 같은 형태로 다시 작성했음
sol2는 sol을 조금 다른 방식으로 표현한 것으로 내용 상 크게 다른 점은 없음   

제출일 기준 python 실행시간 3위, 메모리 1위(sol2)
'''