def solution(price, money, count): #이용료, 소지금, 탑승 횟수
    answer=(1+count)*count/2*price-money
    return answer if answer>0 else 0

'''
평균 실행 시간 : 0.001 평균 메모리 사용량: 10.097

처음에는 sum(range(count+1))을 썼다가 어 이거? 하고 등차 수열의 합으로 구했다 훨 빠름 굿
'''