from collections import Counter
def solution(X, Y): #정수 X,Y
    X=Counter(X)
    Y=Counter(Y)
    ans=""
    xy=X&Y #Counter 만든 후, 교집합으로 공통으로 나타나는 정수
    if not xy:
        return "-1"
    for i,j in sorted(xy.items(),reverse=True): #큰 수부터 붙인다
        ans+=i*j
    if ans.lstrip("0")=="":
        return "0"
    return ans

'''
평균 실행 시간 : 81.3 평균 메모리 사용량: 14.79

for문으로 count해서 붙이는 게 생각보다 더 빨랐음,, 역시 심플 이즈 베스트다,, 굿
'''