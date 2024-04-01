def solution(A,B): #배열 A,B
    A.sort()
    B.sort(reverse=True)
    answer=sum(map(lambda a,b:a*b,A,B))
    return answer

'''
평균 실행 시간 : 0.26 평균 메모리 사용량: 10.17

더 짧게 하려면 map 안에서 sorted한 A,B를 넣어도 되겠지만 그러면 경험적으로 성능이 떨어져서 sort한 후에 map을 사용했다
곱의 합을 최소로 하기 위해서는 당연히 큰 수*큰 수를 피해야 함
해서 각각 내림차, 오름차순으로 정렬하여 곱했다
'''