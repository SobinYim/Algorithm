num=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
def solution(s): #문자열
    for i in range(10):
        s=s.replace(num[i],str(i))
    return int(s)

'''
평균 실행 시간 : 0.02 평균 메모리 사용량: 10.36
'''