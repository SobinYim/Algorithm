def solution(array, commands): #숫자 배열, [i,j,k :i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수]
    answer=[]
    for i,j,k in commands:
        answer.append(sorted(array[i-1:j])[k-1]) #슬라이싱 후 정렬한 것에서 k번째 수를 answer에 추가
    return answer

'''
평균 실행 시간 : 0.003 평균 메모리 사용량: 10.157
'''