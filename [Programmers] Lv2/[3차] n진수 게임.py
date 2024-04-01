def solution(n, t, m, p): #진법, 미리 구할 숫자의 개수, 게임 참가자 수, 튜브의 순서
    conv_li=[str(i) for i in range(10)]+list("ABCDEF") #2<=n<=16
    last=conv_li[n-1] #각 진법의 마지막
    def fn_plus(conv_n): #n진법 수 conv_n에 +1
        if conv_n[-1]==last: #마지막 숫자가 last라면
            if len(conv_n)==1: #들어온 conv_n이 1자리라면 자릿수 올려 10 반환
                return "10"
            else:
                return fn_plus(conv_n[:-1])+"0" #last+1하여 재귀+"0"
        else:
            return conv_n[:-1]+conv_li[conv_li.index(conv_n[-1])+1] #last가 아니라면 conv_li에서 다음 숫자를 구해 conv_n+1 반환
    conv_n,ans="0","0" #n진수로 변환한 수 conv_n, ans
    while len(ans)<m*t+m: #미리 구할 숫자의 개수를 넘어가기 전까지
        conv_n=fn_plus(conv_n)
        ans+=conv_n
    return ans[p-1::m][:t]
'''
평균 실행 시간 : 3.01 평균 메모리 사용량: 10.21

while로 10진수를 k진수로 변환시키는 방법을 많이 쓰는 것 같았는데 매번 변환시키는 건 비효율적이지 않을까 해서 재귀로 k진수 수 n에 +1한 값을 구하는 방식을 사용했다
실제로 빠르게 나와서 만족!
'''