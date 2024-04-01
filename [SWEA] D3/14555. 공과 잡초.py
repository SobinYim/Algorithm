T=int(input()) #tc 개수
for t in range(1,T+1):
    s=input() #문자열
    res=sum(s.count(i) for i in ["()","(|","|)"]) #(), (|, |)를 COUNT
    print(f"#{t}",res)

'''
제출일 기준 python 코드길이 1위
'''