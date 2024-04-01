def solution(want, number, discount): #원하는 제품, 수량, 할인하는 제품 목록
    answer=0
    for i in range(len(discount)-9):
        item=discount[i:i+10] #10개씩 슬라이싱
        for w,n in zip(want,number):
            if item.count(w)!=n: #슬라이싱한 리스트에서 w이 n개가 아니라면 break
                break
        else: #슬라이싱한 리스트에서 원하는 제품을 모두 할인 받을 수 있다면 ans+=1
            answer+=1
    return answer

'''
평균 실행 시간 : 23.31 평균 메모리 사용량: 12.51
'''