def solution(data, ext, val_ext, sort_by): #데이터, 조건 대상 column, 조건(val_ext 미만), 정렬 기준
    col=["code", "date", "maximum", "remain"] #column 순서
    idx_ext=col.index(ext)
    idx_sort=col.index(sort_by)
    answer=sorted([i for i in data if i[idx_ext]<val_ext],key=lambda x: x[idx_sort])
    return answer

'''
평균 실행 시간 : 0.0474 평균 메모리 사용량: 10.26

PCCE 기출이라 그런지 정답률에 비해 아주 무난했던 문제
그래서인지 다른 사람의 풀이도 거의 비슷했다
리스트 컴프리헨션을 쓰느냐 마느냐, index를 저장하느냐 마느냐, column을 딕셔너리로 저장하느냐 리스트로 저장하느냐 정도의 차이?
'''