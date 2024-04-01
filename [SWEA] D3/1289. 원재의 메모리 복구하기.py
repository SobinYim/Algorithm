T=int(input()) #tc 개수
for t in range(1,T+1):
    i="0"+input() #초기화 상태가 0이므로
    res=sum(1 if i[x-1]!=i[x] else 0 for x in range(1,len(i))) #연속된 두 숫자가 다를 시 1, 같으면 0인 합
    print(f"#{t}",res)

'''
제출일 기준 python 코드길이 7위
'''