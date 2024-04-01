ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    a,b,c=map(int,input().split()) #현미 빵의 가격, 단호박 빵의 가격, 은비가 소지한 금액
    a,b=min(a,b),max(a,b) #상대적으로 저렴한 빵이 a, 다른 하나가 b
    res=c//a+c%a//b #은비의 소지금을 a로 나눈 몫과 그 나머지를 b로 나눈 몫의 합
    ans.append(f"#{t} {res}")
for a in ans:
    print(a)

'''
제출일 기준 python 실행시간 14위
'''