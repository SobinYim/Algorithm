#sol
T=int(input())
for t in range(1,T+1):
    n=int(input())
    res="Alice" if n%2==0 else "Bob"
    print(f"#{t}",res)

#sol1
print(*[f"#{t+1} Alice" if int(input())%2==0 else f"#{t+1} Bob" for t in range(int(input()))],sep="\n")

'''
sol과 sol1은 같은 내용
sol1은 심심해서 짜본 건데 실행 시간은 별 차이 없었고 print+컴프리헨션으로 냅다 찍는 게 메모리는 더 적게 잡혔다 

제출일 기준 python 실행시간 1위
'''