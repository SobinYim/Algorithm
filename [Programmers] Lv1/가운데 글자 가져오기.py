from math import ceil
def solution(s): #문자열
    l=ceil((len(s)+1)/2)
    answer=s[-l:l]
    return answer

'''
평균 실행 시간 : 0.007 평균 메모리 사용량: 10.13

if-else를 안 쓰고 푸는 것을 목표로 풀어봤는데,,
다른 사람의 풀이에 s[(len(s)-1)//2:len(s)//2+1]로 구하는 풀이를 봤다
변수 안 쓰고 간단하고 실행 시간도 무려 0.0ms
괜히 돌아서 푼 것 같은 기분이다,, 와하하
'''