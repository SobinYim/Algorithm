ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    n=int(input()[-1]) #홀짝을 판별하기 위해서는 1의 자리 숫자만 있으면 되므로
    res="Odd" if n%2==1 else "Even"
    ans.append(f"#{t} {res}")
for a in ans:
    print(a)