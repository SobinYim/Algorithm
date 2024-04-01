def solution(s): #0과 1로 이루어진 문자열
    r,cnt=0,0 #이진 변환의 횟수, 제거된 0의 개수
    while s!="1":
        s=bin(len(s)-(tmp:=s.count("0")))[2:] #0을 제거한 s의 길이를 2진법으로
        cnt+=tmp
        r+=1
    return [r,cnt]

'''
평균 실행 시간 : 0.09 평균 메모리 사용량: 10.22
'''