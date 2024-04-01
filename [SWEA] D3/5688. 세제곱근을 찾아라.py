T=int(input()) #tc 개수
for t in range(1,T+1):
    n=int(input()) #정수 n
    res=round(n**(1/3)) #주어진 정수의 세제곱근을 반올림(int는 버림이라 round를 사용)
    if res**3!=n: res=-1 #세제곱근 결과 값을 세제곱한 값이 n과 같지 않으면 -1
    print(f"#{t}",res)
    
'''
제출일 기준 python 실행시간 5위, 코드길이 2위, 메모리 1위
'''