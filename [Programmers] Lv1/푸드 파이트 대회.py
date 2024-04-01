def solution(food): #음식의 양
    s = "".join([str(idx)*(item//2) for idx,item in enumerate(food)])
    return s+"0"+s[::-1] #0을 중심으로 각 음식의 개수를 2로 나눈 몫만큼 붙인 것의 회문

'''
평균 실행 시간 : 0.01 평균 메모리 사용량: 10.11
'''