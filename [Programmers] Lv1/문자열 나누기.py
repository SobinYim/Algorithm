def solution(s): #문자열
    ans=1 #기본 개수
    cnt,cnt_x=0,1 #x가 아닌 글자 수, x 등장 횟수
    x=""
    for i in s[:-1]:
        if not x: #x 지정
            x=i
            continue
        if i==x:
            cnt_x+=1
        else:
            cnt+=1
            if cnt==cnt_x: #같아지면 문자열 분리, x 초기화
                cnt,cnt_x=0,1
                x=""
                ans+=1
    return ans

'''
평균 실행 시간 : 0.35 평균 메모리 사용량: 10.2
'''