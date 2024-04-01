def solution(n): #자연수
    ans=0
    while True:
        if n%2: #점프
            n-=1
            ans+=1
            if not n: #else block에서는 n이 0이 될 수 없다
                break
        else: #순간이동
            n/=2
    return ans

'''
[효율성 테스트] 평균 실행 시간 : 0.013 평균 메모리 사용량: 10.079

n부터 역으로 계산한다

def solution(n):
    return bin(n).count('1')
이 풀이 보고 생각해보니까 이게 맞다...
오히려 어떻게 이걸 생각 못 했을까 싶다 ans+=1 대신 ans+="1" 쓰고 else에서 ans+="0" 쓰면 이진수 변환하는 코드인데 하핫
위 코드는 무려 평균 실행 시간 0.0ms다
'''