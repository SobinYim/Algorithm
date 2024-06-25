#sol1
def solution(gems): #진열된 보석의 이름
    buying_yet = set(gems) #아직 구매하지 않은 보석
    gem_cnt = dict((i, 0) for i in buying_yet) #보석을 구매한 횟수
    mn = 0 #최소 인덱스
    r = len(gems) #최소 구간 길이
    ans = [1, len(gems)]
    for idx, i in enumerate(gems):
        gem_cnt[i] += 1
        buying_yet.discard(i)
        if not buying_yet: #모든 보석을 한 번씩 구매했다면 범위를 좁힌다
            while True:
                tg_gem = gems[mn] #가장 왼쪽에 진열된 보석
                gem_cnt[tg_gem] -= 1
                mn += 1
                if not gem_cnt[tg_gem]: #보석이 구매한 범위에 없다면
                    buying_yet.add(tg_gem)
                    break
            if r > (new_r := idx - mn): #최소 구간 길이 경신 시 ans, r 업데이트
                ans = [mn, idx + 1]
                r = new_r
    return ans

#sol2 [시간 초과]
def solution(gems): #진열된 보석의 이름
    gem_idx = dict((i, gems.index(i)) for i in set(gems)) #각 보석의 가장 왼쪽 위치
    mx, mn = max(gem_idx.values()), min(gem_idx.values()) #인덱스 최댓값, 최솟값
    ans = [mn + 1, mx + 1]
    r = mx - mn #최소 구간 길이
    for idx, i in enumerate(gems):
        prev_gem_idx = gem_idx[i]
        gem_idx[i] = idx #인덱스 갱신
        if idx > mx:
            mx = idx
        if prev_gem_idx == mn: #해당 보석의 이전 위치가 최솟값이었다면
            mn = min(gem_idx.values()) #최솟값 갱신
            if r > (tmp := mx - mn): #최소 구간 길이 경신 시 ans, r 업데이트
                r = tmp
                ans = [mn + 1, mx + 1]
    return ans


'''
sol1
[효율성 테스트] 평균 실행 시간 : 14.47 평균 메모리 사용량: 13.53
sol2
[효율성 테스트] 평균 실행 시간 : 143.61 평균 메모리 사용량: 13.73

sol2로 짜다가 효율성 테케 3번이 안 풀려서 sol1로 틀었다

처음에는 모든 보석을 한 번씩은 구매하였는지를 0 not in gem_cnt.values()로 검사했는데
아무리 봐도 비효율적인 것 같아서 보석 집합에서 해당 순회에서 등장한 보석을 제거하는 방식을 사용했다
set().discard()는 없는 요소를 제거한다고 ValueError가 나지는 않아서 편했다
훨씬 직관적으로 동작하는 것 같아서 만족!

인상 깊었던 다른 사람의 풀이:
def solution(gems):
    answer = [0,len(gems)]
    dic = {}
    kind = len(set(gems))
    flag = False
    mini = 0
    min_gem = gems[0]
    for i, gem in enumerate(gems):
        dic[gem] = i
        if min_gem == gem:
            mini = min(dic.values())
            min_gem = gems[mini]
        if flag == False and len(dic) == kind:
            flag = True
        if flag == True:
            if answer[1]-answer[0] > i - mini:
                answer = [mini+1, i+1]
    return answer
[효율성 테스트] 평균 실행 시간 : 12.36 평균 메모리 사용량: 13.47
sol2를 이런 느낌으로 짜고 싶었는데 하하...ㅠ
현재 보석이 최소 인덱스의 보석과 같다면 최소 인덱스를 갱신하고
모든 보석이 등장한 이후부터 최소 인덱스 mini와 현재 인덱스(최대 인덱스) i로 최소 구간 길이를 구한다
'''