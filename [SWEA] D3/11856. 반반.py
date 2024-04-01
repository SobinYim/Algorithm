T=int(input()) #tc 개수
for t in range(1,T+1):
    s=input() #문자열
    res="Yes" if len(set(s))==s.count(s[0]) else "No" #중복을 제거한 값과 값 하나의 개수가 같을 때(==2일 때) "Yes"를 아니면 "No"
    print(f"#{t}",res)
    
'''
제출일 기준 python 코드길이 3위
'''