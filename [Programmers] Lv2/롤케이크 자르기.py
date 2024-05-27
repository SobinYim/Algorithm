from collections import Counter
def solution(topping):
    ans = 0
    c = Counter(topping)
    left = set()
    diff = len(c)
    for t in topping:
        c[t] -= 1
        if t not in left:
            left.add(t)
            diff-=1
        if not c[t]:
            diff-=1
        if not diff:
            ans += 1
        elif diff<0:
            break
    return ans

'''
평균 실행 시간 : 197.97 평균 메모리 사용량: 37.47

더 좋은 방법이 생각은 안 나고,, 테케 실행 시간은 막 400ms가 나와서 살짝 절망했는데
다른 사람들 풀이 보니까 나만 그런 게 아니었다 휴
처음에는 왼쪽 길이, 오른쪽 길이를 각각 저장했는데 
생각해 보니까 어차피 같은지 비교하는데 길이의 차이를 저장하면 되지 않나 해서 diff로 만들어줬다
또 더 검사할 필요가 없어지면 break하여 소소하게 시간을 절약했다

인상 깊었던 다른 사람의 풀이:
def solution(topping):
    db, dic = [], {}
    for i,top in enumerate(topping):
        if top in dic.keys():
            dic[top][1] = i
        else:
            dic[top] = [i,i]
    for val in dic.values():
        db.extend(val)
    db.sort()
    return db[len(db)//2]-db[len(db)//2-1]
평균 실행 시간 : 141.67 평균 메모리 사용량: 37.53
보고 진짜 박수쳤다
이런 코드를 짜고 싶은데 쉽지가 않다
토핑별로 각 방향에서 가장 가까운 인덱스를 저장하고
이를 정렬해서 가운데 두 지점의 차로 구한다
캬 
'''