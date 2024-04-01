def solution(n): #자연수 n
    if n in [1,2]:
        return 1
    answer=1
    for i in range(1,n//2+2): #1부터 n/2 지점까지(그 이상은 볼 필요 없음)
        for j in range(i+1,n//2+3): #i부터 n/2+1 지점까지
            s=int((i+j-1)*(j-i)*.5) #등차수열의 합
            if s>n:
                break
            if s==n: #n과 같으면 answer+1
                answer+=1
    return answer

'''
[효율성 테스트] 평균 실행 시간 : 8.82 평균 메모리 사용량: 10.15

등차수열을 이용해 풀기는 했는데 조금 더 생각을 했어야 했다... 조금 아쉬운 문제

다른 사람의 풀이
len([i for i in range(1,n+1,2) if n%i is 0])
햐 이거 진짜 내 스타일... 심플하고 보자마자 이해 딱 되고 성능 좋고 아주 좋다...
왜 is를 썼는지는 모르겠다.. 더 빠른가....? 
>> ==0보다 더 빠르다! 와 새로운 걸 알았다
>> not n%i도 해봤는데 제일 빠르다 :: not > is > == (0.17ms>0.3ms>0.42ms)
'''