def solution(s, skip, index): #문자열, 건너뛸 알파벳, 밀어낼 숫자
    skip=[ord(i) for i in skip] #skip의 알파벳을 유니코드 포인트로
    dec_dict=dict() #알파벳 변환 딕셔너리
    for i in range(97,97+26):
        tmp=i
        remain_idx=index
        while remain_idx:
            tmp+=1
            tmp=tmp if tmp<123 else tmp-26 #범위를 넘어가면 다시 a부터
            if tmp in skip:
                continue
            else:
                remain_idx-=1
        dec_dict[chr(i)]=chr(tmp)
    return "".join(dec_dict[i] for i in s) #대상 문자열 규칙대로 암호화

'''
평균 실행 시간 : 0.09 평균 메모리 사용량: 10.25
'''