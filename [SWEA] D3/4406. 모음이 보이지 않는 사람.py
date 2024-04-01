#sol
T=int(input()) #tc 개수
for t in range(1,T+1):
    s=input() #문자열
    for i in "aeiou": #replace 메서드를 이용해 모음 제거
        s=s.replace(i,"")
    print(f"#{t}",s)

#sol2
T=int(input()) #tc 개수
for t in range(1,T+1):
    s=input() #문자열
    li=[i for i in s if i not in "aeiou"] #for문과 if문을 이용한 모음 제거
    print(f"#{t}","".join(li))

'''
제출일 기준 python 코드길이 9위
'''