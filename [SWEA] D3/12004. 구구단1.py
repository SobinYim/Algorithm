#sol
T=int(input()) #tc 개수
for t in range(1,T+1):
    n=int(input()) #정수
    res="No"
    for i in range(1,10): #1~9 사이의 수로 나눈 몫이 1~9 사이이고, 나머지가 0이라면 "Yes"
        if n%i==0 and 0<n/i<10:
            res="Yes"
    print(f"#{t}",res)

#sol2
m=set() #구구단
for i in range(1,10):
    for j in range(1,10):
        m.add(i*j)
T=int(input()) #tc 개수
for t in range(1,T+1):
    n=int(input()) #정수
    res="Yes" if n in m else "No" #정수 n이 구구단 리스트에 들어있으면 "Yes"
    print(f"#{t}",res)

'''
제출일 기준 python 코드길이 5위
'''