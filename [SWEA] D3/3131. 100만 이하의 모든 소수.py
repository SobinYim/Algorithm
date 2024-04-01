n=10**6+1
res=[1]*n
for i in range(2,n):
    if res[i]==1:
        for j in range(2*i,n,i):
            res[j]=0
print(*[i for i in range(2,n) if res[i]==1])

'''
에라토스테네스의 체
2부터 n까지의 숫자를 차례로 쓰는데 숫자 i의 리스트 요소가 1이면 i의 배수의 요소를 모두 0으로 바꾸어 줌
이를 반복하면 리스트의 요소가 1인 수는 모두 소수가 됨 
'''