#sol1
seq=[1,1]
for i in range(2, 2000): #1<n<2000
    seq.append((seq[i-2]+seq[i-1])%1234567)
def solution(n): #칸 수
    return seq[n]

#sol2
def solution(n): #칸 수
    x,y=1,1
    for i in range(n):
        x,y=y,x+y
    return x%1234567

'''
#sol1
평균 실행 시간 : 0.0 평균 메모리 사용량: 10.3
#sol2
평균 실행 시간 : 0.05 평균 메모리 사용량: 10.15

sol1은 그냥 꼼수고 정석대로 풀면 sol2와 같다
피보나치 수라는 걸 다른 사람들은 어떻게 알았는지 모르겠는데 그냥 규칙으로 찾았다
'''