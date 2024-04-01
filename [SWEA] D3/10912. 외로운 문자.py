T=int(input()) #tc 개수
for t in range(1,T+1):
    s=input() #문자열
    li=[i for i in set(s) if s.count(i)%2==1] #문자열의 중복을 제거한 값(==문자열의 구성 요소)를 카운트하고 이 값이 홀수이면 리스트에 추가
    res="".join(sorted(li) if li else "Good")
    print(f"#{t}",res)

'''
제출일 기준 python 코드길이 1위  
'''