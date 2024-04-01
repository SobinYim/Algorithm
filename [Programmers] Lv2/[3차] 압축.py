def solution(msg): #문자열
    ans=[]
    lzw_dict=dict([(chr(i),i-64) for i in range(65,65+26)]) #사전 초기화
    cnt=27 #사전 색인 번호
    while msg:
        for i in range(1,len(msg)+1):
            if (tmp:=msg[:i]) not in lzw_dict.keys(): #msg의 부분 문자열이 사전에 없을 경우
                ans.append(lzw_dict[prev]) #직전 색인 번호
                lzw_dict[tmp]=cnt #사전에 현재 부분 문자열 추가
                cnt+=1
                break
            prev=msg[:i]
        else: #문자열 끝에서
            i+=1
        msg=msg[i-1:] #재할당
    return ans+[lzw_dict[tmp]]

'''
평균 실행 시간 : 0.33 평균 메모리 사용량: 10.22
'''