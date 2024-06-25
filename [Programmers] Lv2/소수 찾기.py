#sol1
from itertools import permutations as perm
def solution(numbers): #종이 조각에 적힌 숫자
    case = set()
    for i in range(1, len(numbers) + 1): #경우의 수
        case = case.union(perm(numbers, i))
    ans = 0
    visited = {0, 1} #이미 검사한 수
    for i in case:
        n = int("".join(i)) #int형으로 변환
        if n in visited: #이미 검사한 수라면 continue
            continue
        visited.add(n)
        for j in range(2, int(n ** .5) + 1): #소수인지 검사
            if not n % j:
                break
        else: #어떤 수로도 나누어 떨어지지 않는다면 ans += 1
            ans += 1
    return ans

#sol2
from collections import Counter
def can_form(n): #검사할 수 -> 종이 조각으로 만들 수 있는 숫자인지 검사
    c = numbers_c.copy()
    while n:
        n, k = divmod(n, 10)
        if k not in c.keys():
            return False
        else:
            c[k] -= 1
            if not c[k]:
                c.pop(k)
    return True
def solution(numbers): #종이 조각에 적힌 숫자
    global numbers_c
    ans = 0
    p = [0] * (tmp := (int("".join(sorted(numbers, reverse=True))) + 2))
    numbers_c = Counter(map(int, numbers))
    for i in range(2, tmp): #에라토스테네스의 체
        if p[i]:
            continue
        else:
            for j in range(i*i, tmp, i):
                p[j] = 1
            ans += can_form(i)
    return ans

'''
sol1
평균 실행 시간 : 0.98 평균 메모리 사용량: 10.47
sol2
평균 실행 시간 : 315.67 평균 메모리 사용량: 17.28

set를 이용해 중복을 제거함으로써 불필요한 실행을 줄였다
0과 1은 다른 수로 나누어떨어지지 않으면서 소수가 아니므로 visited에 미리 추가해 주었다

sol1은 종이 조각으로 수를 만든 후 소수가 맞는지 검사하는 방식이라면
sol2는 소수를 찾은 후 종이 조각으로 만들 수 있는 수 인지 검사한다
에라토스테네스의 체 자체가 수가 커질수록 효율성이 떨어지는 건 알고 있었는데 이렇게 차이가 크게 날 줄은 몰랐다
permutations 사용으로 조금 오래 걸릴 줄 알았는데 sol1은 생각보다 시간 소모가 적었다
'''