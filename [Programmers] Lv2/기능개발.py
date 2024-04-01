from math import ceil
def solution(progresses, speeds): #진행도, 개발 속도(정렬-배포되어야 하는 순서)
    mx,cnt=0,0 #최댓값, 배포할 기능 수
    answer=[]
    for p,s in zip(progresses,speeds):
        i=ceil((100-p)/s) #기능 완성 예정일
        if i>mx: #현재 순회하는 기능 완성 예정일이 기존 최댓값보다 크다면
            mx=i
            answer.append(cnt)
            cnt=0
        cnt+=1
    if cnt:
        answer.append(cnt)
    return answer[1:] #처음에 mx가 0으로 저장되어 있어 들어가는 값 제외하고

'''
평균 실행 시간 : 0.01 평균 메모리 사용량: 10.24

기능 완성 예정일 최댓값이 업데이트되면 그전까지 개발된 기능들을 배포한다
기능 완성 예정일이 다음과 같다면
[5,1,6,1,7,1,6,1,1]
이는 이것과 같다
[5,5,6,6,7,7,7,7,7]
'''