def solution(nums): #폰켓몬 배열
    return min(len(set(nums)),len(nums)//2) #폰켓몬의 종류와 폰켓몬 길이의 절반 중 적은 쪽을 반환

'''
평균 실행 시간 : 0.12 평균 메모리 사용량: 10.14
'''