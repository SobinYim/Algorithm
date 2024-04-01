#sol1
def solution(n): #자연수 n
    tmp=""
    while n:
        tmp+=str(n%3)
        n=n//3
    answer = int(tmp,3)
    return answer

#sol2
li=[3**i for i in range(16,-1,-1)] #3의 n제곱을 구해주고 시작
def solution(n): #자연수 n
    tmp=""
    for i in li:
        tmp+=str(n//i)
        n=n%i
    answer=sum(map(lambda x: int(x[0])*x[1], zip(tmp.lstrip("0"),li[::-1])))
    return answer

'''
#sol1
평균 실행 시간 : 0.02 평균 메모리 사용량: 10.33
#sol2
평균 실행 시간 : 0.03 평균 메모리 사용량: 10.36

대략 사파 코드(sol2)이랑 정석 코드라 보면 되겠다
왜 저렇게 짰는지는 모르겠음,,(???)
'''