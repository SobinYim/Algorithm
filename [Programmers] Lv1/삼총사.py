def solution(number): #정수 번호 목록
    answer=0
    l=len(number)
    for i in range(l): #조합
        n1=number[i]
        for j in range(i+1,l):
            n2=number[j]
            for k in range(j+1,l):
                if n1+n2+number[k]==0:
                    answer+=1
    return answer

'''
평균 실행 시간 : 0.04 평균 메모리 사용량: 10.2

n1, n2 할당 없이도 돌려봤는데 큰 차이 없었다(0.02ms 느렸음)
combinations을 사용해도 무방하나 어려운 것도 아니고 해서 for문으로 구현했다
'''