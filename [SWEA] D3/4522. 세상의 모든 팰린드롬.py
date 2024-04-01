T=int(input()) #tc 개수
for t in range(1,T+1):
    s=input() #문자열
    res="Exist"
    for i in range(len(s)//2):
        if s[i]!=s[-(i+1)] and "?" not in [s[i],s[-(i+1)]]: #문자열의 양 i번째 요소가 다르고, 와일드카드도 아니라면 "Not exist"
            res="Not exist"
            break
    print(f"#{t} {res}")

'''
제출일 기준 python 코드길이 1위
'''