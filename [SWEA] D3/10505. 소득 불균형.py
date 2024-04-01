ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    n=int(input()) #집단 수
    li=sorted(list(map(int,input().split())),reverse=True) #소득 리스트를 내림차순 정렬
    mean=sum(li)/len(li)
    res=0
    for i in li: #i가 평균과 같거나 커지면 해당 인덱스를 전체 길이에서 뺀 값을 res에 저장하고 반복 중지
        if i<=mean:
            res=len(li)-li.index(i)
            break
    ans.append(f"#{t} {res}")
for a in ans:
    print(a)

'''
제출일 기준 python 실행시간 3위
'''