def solution(strings, n): #문자열 리스트, 정렬 기준
    return sorted(strings,key=lambda x:(x[n],x)) #n번째 문자를 기준으로 정렬, 우선도가 같으면 사전 순으로

'''
평균 실행 시간 : 0.01 평균 메모리 사용량: 10.17

key를 튜플을 이용해 지정해 주었는데,, 다른 풀이 보니까 x[n]만으로도 작동하는 모양이다,,
'''