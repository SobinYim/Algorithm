ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    s=input() #문자열
    res=len(s) #결과 값 초기화
    for i,j in enumerate(s):
        if i!=ord(j)-97: #ord("a")==97 이므로 97을 뺀 값과 문자열의 인덱스 값과 다르다면 break
            res=i
            break
    ans.append(f"#{t} {res}")
for a in ans:
    print(a)

'''
제출일 기준 python 실행시간 1위
'''