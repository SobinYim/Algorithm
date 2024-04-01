k=1234567891 #나눌 값
f=[1] #factorial % 1234567891
for i in range(1,1000001):
    f.append((f[i-1]*i)%k)
ans=[] #한 번에 출력하기 위해
T=int(input()) #tc 개수
for t in range(1,T+1):
    n,r=map(int,input().split()) #n combination r
    d=pow(f[r]*f[n-r],k-2,k) # *
    res=f[n]*d%k # **
    ans.append(f"#{t} {res}")
for a in ans:
    print(a)

'''
*
페르마의 소정리를 이용하기 위하여 조합식을 거듭제곱(n! * (r!(n-r)!)**p-2) 문제로 바꿈
pow함수를 이용해 (r!(n-r)!)**p-2를 k로 나누어 준 나머지를 구함(시간 절약 차원에서 나머지를 구함)
**
위 결과를 n!과 곱한 후, k로 나눈 나머지를 구함

**페르마의 소정리**
p=소수, a,p=서로소
a**p % p == a
a**(p-1) % p == 1
a**(p-2) % p == a**-1
이를 이용하여
n! * (r!(n-r)!)**-1 를
n! * (r!(n-r)!)**p-2 로 만들어 p로 나눠 답을 구할 수 있음

pow(x,y) == x**y
pow(x,y,z) == x**y//z

조금 힘들었던 문제,,
'''