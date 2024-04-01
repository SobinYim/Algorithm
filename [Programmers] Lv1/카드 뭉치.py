def solution(cards1, cards2, goal): #카드 뭉치1, 카드 뭉치2, 목표 단어 배열
    for i in goal:
        if i in cards1[:1]: #카드 뭉치가 비었을 때 인덱스 에러를 피하기 위해 슬라이스
            cards1.pop(0)
        elif i in cards2[:1]:
            cards2.pop(0)
        else: return "No"
    return "Yes"

'''
평균 실행 시간 : 0.007 평균 메모리 사용량: 10.224

맨 앞의 카드가 목표 단어인 뭉치에서 pop(0), 목표 단어가 없다면 "No" 리턴
deque는 슬라이싱 지원이 안되기도 하고, 카드 뭉치의 길이가 길지 않아서 리스트 사용
'''