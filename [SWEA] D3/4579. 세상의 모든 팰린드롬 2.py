T=int(input()) #tc 개수
for t in range(1,T+1):
    s=input().split("*") #와일드카드를 기준으로 split
    sl=min(len(s[0]),len(s[-1])) #와일드카드 *은 어떤 문자라도 들어갈 수 있으므로 더 짧은 쪽을 기준으로 양쪽을 비교
    res="Exist" if s[0][:sl]==s[-1][::-1][:sl] else "Not exist" #양쪽이 동일하다면 팰린드롬
    print(f"#{t} {res}")

'''
제출일 기준 python 실행시간 1위, 코드길이 1위
'''