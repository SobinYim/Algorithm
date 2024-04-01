def solution(n): #1부터 n 사이의 소수의 수
    ans=0
    p=[0]*(n+1)
    p[:2]=1,1
    for i in range(2,n+1): #에라토스테네스의 체
        if p[i]:
            continue
        for j in range(i*i,n+1,i):
            p[j]=1
        ans+=1
    return ans

'''
[효율성 테스트] 평균 실행 시간 : 131.87 평균 메모리 사용량: 16.95

p.count(0)을 해줘도 되겠지만 n이 커지면 차라리 새로 변수를 만들어 쓰는 편이 효율 면에서 나을 것 같아서 소수일 때 ans를 증가시키는 방법을 썼다
'''