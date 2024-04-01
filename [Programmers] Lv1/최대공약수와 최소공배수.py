def solution(a, b): #정수 a, b
    a,b=(a,b) if a<b else (b,a) #b가 큰 수
    div_a,div_b=set(),set() #약수
    for i in range(1,min(a,int(b**.5)//1)+1): #약수 구하기(a와 b의 제곱근 중 작은 수까지)
        if a%i==0:
            div_a.update([i,a//i])
        if b%i==0:
            div_b.update([i,b//i])
    cd=max(div_a&div_b) #최대 공약수
    cm=a*b//cd #최소 공배수
    return [cd,cm]

'''
평균 실행 시간 : 0.02 평균 메모리 사용량: 10.17

최대 공약수는 정말 정직하게 a와 b의 약수 중 최댓값을 반환했고 
최소 공배수를 처음에 (a//cd)*(b//cd)*cd로 구했다가 엥? 하고 a*b//cd로 정리해주었다 

유클리드 알고리즘을 이용해서 구현하면 아래와 같다:
def solution(a, b):
    c,d = max(a, b), min(a, b)
    while d:
        c, d = d, c % d
    answer = [c, int(a*b/c)]
    return answer
진짜 멋있다.. 나는 역시 수학으로 구현한 코드가 좋다
무려 실행 시간 0.0ms 다... 코드 예쁘고 성능 좋고 햐,,
확실하게 기억해 놔야겠다,,  a=bq+r이면 G(a,b)=G(b,r)
'''