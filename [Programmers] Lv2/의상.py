from functools import reduce
def solution(clothes): #[옷, 옷의 카테고리]로 이루어진 배열
    d=dict() #카테고리:종류 딕셔너리
    for _,i in clothes:
        if i in d.keys(): #해당 옷 카테고리가 딕셔너리에 존재한다면
            d[i]+=1
        else:
            d[i]=2 #착용하지 않는다는 선택지까지
    answer=reduce(lambda x,y: x*y,d.values())-1 #'모두 착용하지 않는다' 제외한 경우의 수
    return answer

'''
평균 실행 시간 : 0.01 평균 메모리 사용량: 10.19
'''