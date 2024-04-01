#sol1
def solution(absolutes, signs): #정수 배열, 부호
    answer=sum(absolutes)-sum([absolutes[idx] for idx, i in enumerate(signs) if not i])*2 #전체 합 - sign이 False인 수의 합*2
    return answer

#sol2
def solution(absolutes, signs): #정수 배열, 부호
    answer=0
    s=[-1,1] #boolean 값으로 부호를 가져와서 연산
    for i in range(len(signs)):
        answer+=absolutes[i]*s[signs[i]]
    return answer

'''
#sol1
평균 실행 시간 : 0.07 평균 메모리 사용량: 10.16
#sol2
평균 실행 시간 : 0.15 평균 메모리 사용량: 10.18

zip함수를 생각 못해서 조금 돌아갔다,, 아쉽
느리긴 하지만 sum([2*x*y - x for x, y in zip(absolutes, signs)])도 예쁜 것 같다,,
'''