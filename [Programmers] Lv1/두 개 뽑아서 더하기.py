def solution(n): #정수 배열
    answer=set() #덧셈 결과
    for i in range(len(n)): #조합
        for j in range(i+1,len(n)):
            answer.add(n[i]+n[j])
    answer=sorted(answer)
    return answer

'''
평균 실행 시간 : 0.18 평균 메모리 사용량: 10.24
'''