from math import isqrt
def solution(n, k): #양의 진수, k진수 변환
    ans=0
    conv_n=[]
    while n:
        conv_n.append(str(n%k))
        n//=k
    split_n="".join(conv_n)[::-1].split("0") #n을 k진법으로 변환한 결과를 "0"을 기준으로 분리
    for i in split_n:
        if i in ["","1"]:
            continue
        i=int(i)
        for j in range(2,isqrt(i)+1): #소수인지 검사
            if not i%j:
                break
        else: #소수라면
            ans+=1
    return ans

'''
평균 실행 시간 : 5.73 평균 메모리 사용량: 10.26

처음에는 에라토스테네스의 체를 사용하려고 했는데 자꾸 런타임 에러가 나서 풀고 나서 알아보니까 max 값이 너무 커서 그렇다고,,,
'''