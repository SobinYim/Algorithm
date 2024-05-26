def solution(land): #땅
    ans = [0] * (l := len(land[0]))
    for item in land:
        mx_idx = ans.index(max(ans)) #이전까지의 최댓값 인덱스
        mx = ans.pop(mx_idx) #이전까지의 최댓값
        for idx in range(l):
            item[idx] += max(ans) if idx==mx_idx else mx #각 칸을 선택했을 때의 최댓값
        ans = item
    return max(ans)

'''
[효율성  테스트] 평균 실행 시간 : 99.83 평균 메모리 사용량: 29.3

두 번째로 큰 값을 찾아야 해서 무슨 방법을 쓸까 하다가 최댓값을 pop하는 방식을 선택했다
'''
