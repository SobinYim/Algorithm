def solution(data, col, row_begin, row_end): #데이터, 정렬 기준 column, 시작 튜플, 끝 튜플
    data.sort(key=lambda x: (x[col - 1], -x[0])) #정렬
    ans = 0
    for i in range(row_begin - 1, row_end):
        row = i + 1
        S = 0
        for j in data[i]:
            S += j % row
        ans = ans ^ S #XOR 연산
    return ans


'''
평균 실행 시간 : 14.49 평균 메모리 사용량: 34.35

map 사용 풀이와 이중 for문 풀이가 의외로 시간 차이가 조금 났다(map 사용 시 19.35ms)
index를 1부터 세는 관계로 row를 i+1로 만들어줬다

enumerate(data[row_begin - 1 : row_end], row_begin)를 이용하면 row_begin부터 idx가 시작하도록 할 수 있다!
이를 이용하면 row를 다시 만들거나 j % (i+1)와 같이 쓸 필요 없다
'''
