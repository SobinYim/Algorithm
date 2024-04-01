def solution(genres, plays):
    play_dict=dict() #장르:(인덱스, 재생 횟수) 딕셔너리
    for idx,(g,p) in enumerate(zip(genres,plays)):
        if g not in play_dict.keys():
            play_dict[g]=[(idx,p)]
        else:
            play_dict[g].append((idx,p))
    album=[]
    for g,item in sorted(play_dict.items(),key=lambda x:sum([j for i,j in x[1]]),reverse=True): #재생 횟수 합한 것을 키 값으로 정렬
        album+=[i for i,j in sorted(item,key=lambda x:x[1],reverse=True)[:2]] #재생 횟수를 키 값으로 정렬한 것을 슬라이싱하여 리스트에 추가
    return album

'''
평균 실행 시간 : 0.03 평균 메모리 사용량: 10.22

장르별로 딕셔너리에 추가 후 재생 횟수의 합을 키 값으로 내림차순 정렬하고
이렇게 정렬한 장르를 재생 횟수를 키 값으로 정렬하여 앞에서 두 번째까지 슬라이싱하여 앨범에 추가
'''