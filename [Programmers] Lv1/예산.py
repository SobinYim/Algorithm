def solution(d, budget): #신청 금액, 예산
    d.sort() #소액부터 지원해야 최대한 많은 부서에 지원 가능
    for idx,item in enumerate(d):
        budget-=item
        if budget<0:
            return idx #인덱스==지원받은 부서의 수
    return len(d) #모든 부서

'''
평균 실행 시간 : 0.009 평균 메모리 사용량: 10.164
'''