#sol
def solution(n, lost, reserve): #학생 수, 체육복을 도난당한 학생, 여벌 체육복을 가져온 학생
    students=[1]*(n+2) #소지 체육복 수
    for l in lost:
        students[l]-=1
    for r in reserve:
        students[r]+=1
    for idx,i in enumerate(students):
        if i==0: #체육복이 없다면
            if students[idx-1]==2: #앞 번호 학생은 감하나 감하지 않으나 결과는 같다
                students[idx]=1
            elif students[idx+1]==2: #뒷 번호 학생에게 체육복이 있다면 i와 i+1에 1을 할당
                students[idx:idx+2]=[1,1]
    return n-students.count(0)

#sol1
def solution(n, lost, reserve): #학생 수, 체육복을 도난당한 학생, 여벌 체육복을 가져온 학생
    students=[1]*(n+2) #소지 체육복 수
    for l in lost:
        students[l]-=1
    for r in reserve:
        students[r]+=1
    for i in range(1,n+1):
        if students[i]==0: #체육복이 없다면
            if students[i-1]==2: #앞 번호 학생에게 빌리기
                students[i-1]-=1
                students[i]+=1
            elif students[i+1]==2: #뒷 번호 학생에게 빌리기
                students[i+1]-=1
                students[i]+=1
    return n-students.count(0)


'''
#sol
평균 실행 시간 : 0.008 평균 메모리 사용량: 10.24
#sol1
평균 실행 시간 : 0.01 평균 메모리 사용량: 10.23

students 리스트는 여벌, 도난 체육복 처리할 때 인덱스 처리하지 않기 위해 + i+1에서 예외 발생시키지 않기 위해 n+2로 생성하였다
sol1는 sol과 같은 내용
sol에서 약간 날림으로 작성한 부분만 제대로 작성했다
'''