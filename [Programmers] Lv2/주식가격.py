def solution(prices): #주식 가격
    answer=[0]*len(prices) #prices의 길이만큼
    stack=[] #인덱스 저장할 리스트
    for idx,i in enumerate(prices):
        while stack and i<prices[stack[-1]]: #stack이 비어있지 않고 마지막 요소의 prices 값이 현재 prices 값보다 크다면(==가격이 떨어짐)
            j=stack.pop()
            answer[j]=idx-j #인덱스로 가격이 떨어지지 않은 시간 계산
        stack.append(idx)
    while stack: #남아있는 인덱스 처리
        j=stack.pop()
        answer[j]=len(prices)-1-j
    return answer

'''
[효율성 테스트] 평균 실행 시간 : 19.82 평균 메모리 사용량: 18.18

while을 이용하여 현재 가격 i보다 큰 값들을 정리해주기 때문에 stack에 들어있는 index의 prices 값들은 오름차순 정렬되어 있는 것과 같다
'''