#sol
T=int(input()) #tc 개수
for t in range(1,T+1):
    res=int(input())**2 #모든 변이 n인 가장 넓은 정사각형의 넓이는 n*n과 같음
    print(f"#{t}",res)

#sol1
print(*[f"{t+1} {int(input())**2}" for t in range(int(input()))],sep="\n")

'''
sol과 sol1은 같은 내용

제출일 기준 python 실행시간 3위, 코드길이 5위
'''