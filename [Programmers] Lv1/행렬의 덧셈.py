def solution(arr1, arr2): #행렬 1, 행렬 2
    answer=[list() for _ in range(len(arr1))] #행렬의 길이만큼 미리 생성
    for idx,i in enumerate(zip(arr1,arr2)):
        answer[idx]=list(map(sum,zip(*i))) #역치하여 합계
    return answer

'''
평균 실행 시간 : 1.44 평균 메모리 사용량: 11.11
'''