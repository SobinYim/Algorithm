ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    p,q=input().rstrip(),input().rstrip() #p가 q보다 순서상 먼저 오는 문자열
    res="N" if q==p+"a" else "Y" #무한 사전에는 모든 단어가 들어오므로 p 다음으로 오는 단어는 무조건 p+"a"
    ans.append(f"#{t} {res}")
for a in ans:
    print(a)

'''
제출일 기준 python 실행시간 3위
'''