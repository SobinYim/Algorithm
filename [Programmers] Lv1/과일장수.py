from collections import Counter
def solution(k, m, score): #최대 점수, 박스 크기, 점수
    c=Counter(score)
    temp,ans=0,0 #같은 점수의 과일을 담을 임시 변수, 최대 이익
    for i in sorted(c.keys(),reverse=True):
        temp+=c[i]
        ans+=temp//m*i*m
        temp%=m
    return ans

'''
평균 실행 시간 : 9.92 평균 메모리 사용량: 11.97

처음에는 평범하게 리스트를 정렬한 후, 슬라이싱으로 풀었으나 정렬에 시간이 오래 걸리는 관계로 Counter를 이용하여 풀었다
'''