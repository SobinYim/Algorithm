def solution(storey): #엘리베이터 층
    ans=0
    flag=False
    while storey:
        storey,i=divmod(storey,10) #10으로 나눈 몫, 나머지=storey, i
        i+=(flag and i>4) #이전 i가 5이고 현재 i가 5이상이면 i+=1
        flag=False
        if i==5:
            ans+=i
            flag=True
        elif i<5: #버림
            ans+=i
        else: #올림
            ans+=10-i
            storey+=1
    return ans

'''
평균 실행 시간 : 0.002 평균 메모리 사용량: 10.143

round로 뭔가 깔끔하게 될 것 같은데 잘 안 나온다,, 아쉽스
좀 예쁜 코드가 아니라 그렇지 이 방법이 제일 빠르기는 한 것 같다...
루프를 해도 되고 for문으로 len(str(storey))+1 해도 된다
'''