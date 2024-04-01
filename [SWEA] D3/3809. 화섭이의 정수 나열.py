T=int(input()) #tc 개수
for t in range(1,T+1):
    n=int(input().rstrip()) #정수열의 길이
    s="" #정수열 초기화
    while len(s)!=n: #정수열의 길이가 n이 될 때까지 공백을 제거하고 붙여 넣음
        s+=input().replace(" ","")
    tg=0 #찾을 정수 초기화
    while s.find(str(tg))!=-1: #tg가 정수열에 있다면 tg를 늘리고 탐색을 계속함
        tg+=1
    print(f"#{t}",tg)

'''
제출일 기준 python 실행시간 10위, 코드길이 3위
'''