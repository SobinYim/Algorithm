#sol1
def solution(s): #문자열
    answer=""
    idx=0 #단어 인덱스
    for i in s:
        idx+=1
        if i==" ": #공백 등장 시 인덱스 초기화
            idx=0
        answer+=(i.upper() if idx%2 else i.lower()) #인덱스가 홀수면 대문자 짝수면 소문자
    return answer

#sol2
def solution(s): #문자열
    ans=[]
    s=s.split(" ") #공백을 기준으로 나눈다
    for w in s: #단어별로 인덱스가 짝수면 대문자 홀수면 소문자
        tmp="" #처리된 단어 변수 초기화
        for idx,i in enumerate(w):
            if idx%2:
                tmp+=i.lower()
            else:
                tmp+=i.upper()
        ans+=[tmp]
    return " ".join(ans) #join()으로 이어주기

'''
#sol1
평균 실행 시간 : 0.017 평균 메모리 사용량: 10.104
#sol2
평균 실행 시간 : 0.018 평균 메모리 사용량: 10.113

sol2에서 반드시 " "을 기준으로 나눠야 한다 
그냥 split()만 쓰면은 공백이 몇 개이든 알아서 처리를 해주기 때문에,, 공백이 여러 개 들어간다면 예상 결과와 다르게 나와버린다
map을 이용해서 join을 두 번 쓰는 방법도 썼는데 속도도 떨어지고 가독성도 떨어져서 굳이 기록해두지 않겠다
'''