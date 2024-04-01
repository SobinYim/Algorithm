#sol
ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    res=int(input())//3 #학생 수를 3으로 나눈 몫
    ans.append(f"#{t} {res}")
for a in ans:
    print(a)

#sol1
print(*[f"#{t+1} {int(input())//3}" for t in range(int(input()))],sep="\n")

'''
sol과 sol1은 같은 코드
sol1에서 시간적으로는 for문을 이용하는 것이 효율적이겠으나 케이스가 그렇게 크지 않아서 print로 출력
의외로 sol1이 실행 시간이 짧게 나왔다

제출일 기준 python 실행시간 2위, 메모리 2위(sol1)
'''