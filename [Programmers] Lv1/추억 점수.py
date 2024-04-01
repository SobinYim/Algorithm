def solution(name, yearning, photo): #이름, 그리움 점수, 사진에 찍힌 인물의 이름
    mp=dict() #이름[그리움 점수] 딕셔너리
    for idx,item in enumerate(name):
        mp[item]=yearning[idx]
    answer=[]
    for i in photo:
        answer+=[sum(map(lambda x: mp.get(x,0),i))] #그리움 점수의 합(딕셔너리에 없으면 0)
    return answer

'''
평균 실행 시간 : 0.59 평균 메모리 사용량: 10.44
'''