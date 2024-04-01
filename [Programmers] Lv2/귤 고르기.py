from collections import Counter
def solution(k, tangerine): #한 상자에 담으려는 귤 개수, 귤의 크기 배열
    c=Counter(tangerine)
    n=0 #상자에 담은 귤의 수
    for idx,i in enumerate(sorted(c.values(),reverse=True)): #가장 많은 크기부터
        n+=i
        if n>=k:
            break
    return idx+1

'''
평균 실행 시간 : 5.5 평균 메모리 사용량: 12.65

Counter 없이 딕셔너리로도 짰는데 특별히 기록할 만한 부분도 없고 시간(11.42ms) 말고는 큰 차이 없어서 그냥 넘어가기로
'''