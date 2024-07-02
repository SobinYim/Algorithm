#sol1
from itertools import combinations as comb
from collections import Counter, defaultdict
def solution(orders, course): #손님들이 주문한 단품 메뉴, 코스 요리를 구성하는 단품 메뉴들의 갯수
    menu_comb = defaultdict(list) #가능한 코스 메뉴 딕셔너리 (메뉴 수:구성)
    for o in orders: #주문 목록을 순회하며 가능한 모든 메뉴 조합 생성
        ordered_o = sorted(o)
        for i in range(2, len(o) + 1):
            menu_comb[i].extend(comb(ordered_o, i))
    ans = []
    for i in course:
        prev = 0
        for k, v in Counter(menu_comb[i]).most_common(): #코스 메뉴 수에서 가능한 조합의 Counter
            if v < prev or v < 2: #등장 횟수가 이전보다 작아지거나 2회 이상 등장하지 않았을 경우 break
                break
            prev = v
            ans.append("".join(k))
    return sorted(ans)

#sol2
from itertools import combinations as comb
from collections import Counter
def solution(orders, course): #손님들이 주문한 단품 메뉴, 코스 요리를 구성하는 단품 메뉴들의 갯수
    orders = [sorted(i) for i in orders] #주문 목록의 각 주문들 정렬
    ans = []
    for i in course:
        menu_comb = []
        for o in orders:
            menu_comb.extend(comb(o, i)) #코스 요리 수에 따른 가능한 메뉴 조합
        if menu_comb:
            c = Counter(menu_comb).most_common()
            mx = c[0][1] #가장 많이 등장하는 조합의 등장 횟수
            for k, v in c:
                if v != mx or v < 2: #등장 횟수가 mx와 다르거나 2번 이상 등장하지 않았다면 break
                    break
                ans.append("".join(k))
    return sorted(ans)


'''
sol1
평균 실행 시간 : 1.24 평균 메모리 사용량: 10.64
sol2
평균 실행 시간 : 0.61 평균 메모리 사용량: 10.4

sol1>sol2 순으로 짰다
order가 정렬이 안된 값이라는 걸 늦게 알아채서 조금 헤맸다
sol1은 필요하지 않은 코스 조합까지 만들어서 조금 느린 것 같아서 sol2를 짜게 되었다
sol2는 필요한 코스 조합만 생성하여 sol1보다 적게 연산을 하여 빠르긴 하지만 무려 3중 for문이다... 와하핫

sol1은 주문 목록을 순회하며 모든 코스 조합을 구하고 이를 (코스 요리 수 : 구성) 딕셔너리에 담아
Counter의 most_common()을 이용하여 내림차순으로 정렬하여 가장 자주 등장한 코스를 ans에 추가하고 이를 정렬한 값을 return하였다
sol2는 코스 요리 수를 순회하며 필요한 코스 조합을 구하고 이를 list에 담아
마찬가지로 Counter의 most_common()을 이용하여 가장 자주 등장한 코스를 ans에 추가하고 이를 정렬한 값을 return하였다

chain을 쓴 풀이도 있었다!
'''