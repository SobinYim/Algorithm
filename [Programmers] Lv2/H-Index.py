from collections import Counter
def solution(citations): #논문별 인용 횟수
    ans=0
    citations.sort(reverse=True)
    for k,v in Counter(citations).items():
        if k<=ans+v: #논문의 인용 횟수 k가 k 회 이상 인용된 횟수보다 작아지면
            ans=max(ans,k)
            break
        ans+=v
    return ans

'''
평균 실행 시간 : 0.22 평균 메모리 사용량: 10.28

좀 아쉬운 문제,,
Counter 쓸 생각은 했으면서 citations의 인덱스가 k 회 이상 인용된 횟수라는 건 생각을 못 했다..
ㅠㅠ

def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for idx,i in enumerate(citations):
        if i >= l-idx:
            return l-idx
    return 0
평균 실행 시간 : 0.06 평균 메모리 사용량: 10.18
다른 사람의 풀이에서 본 내가 짜고 싶었던 코드,,
아주 깔끔하고,, 빠르고 좋다
'''