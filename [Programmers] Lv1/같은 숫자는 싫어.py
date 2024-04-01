def solution(arr): #배열
    answer=[arr[0]] #첫 번째 요소 넣어주기(인덱스 에러)
    for i in arr:
        if i!=answer[-1]: #마지막 요소와 i가 다르다면 리스트에 추가
            answer.append(i)
    return answer

'''
[효율성 테스트] 평균 실행 시간 : 71.81 평균 메모리 사용량: 27.9
'''