def solution(numbers): #정수 배열
    stack=[] #인덱스 저장
    ans=[-1]*len(numbers) #뒷 큰수 배열
    for idx,i in enumerate(numbers):
        while stack and numbers[stack[-1]]<i: #stack이 비어있지 않고 stack의 마지막으로 저장된 인덱스의 numbers 값이 순회중인 numbers의 요소보다 작으면 루프
            ans[stack.pop()]=i #stack에 마지막으로 담긴 인덱스에 뒷 큰수 i 저장
        stack.append(idx)
    return ans

'''
평균 실행 시간 : 104.49 평균 메모리 사용량: 41.52

stack 안 인덱스의 값은 자연스럽게 내림차순 정렬이 되어있으므로 맨 마지막 요소들만 확인하면 된다
의외로 enumerate를 쓰느냐 인덱스로 값을 가져오느냐에 따라 실행 시간 차이가 있었다
다른 사람의 풀이 최상단 풀이와 거의 동일하게 풀었는데 enumerate가 약 20ms 빨랐다
'''