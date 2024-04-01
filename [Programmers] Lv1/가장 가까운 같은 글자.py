def solution(s): #문자열
    answer=[]
    loc_dict=dict() #알파벳 등장 위치 딕셔너리
    for idx,i in enumerate(s):
        if i not in loc_dict: #최초 등장
            answer.append(-1)
        else:
            answer.append(idx-loc_dict[i])
        loc_dict[i]=idx #갱신
    return answer

'''
평균 실행 시간 : 0.45 평균 메모리 사용량: 10.33
'''