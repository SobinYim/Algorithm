#sol1
def solution(answers): #정답
    s1,s2,s3=[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5] #학생 1,2,3이 찍는 패턴
    l1,l2,l3=len(s1),len(s2),len(s3) #길이
    score=[0]*3 #점수
    for idx,i in enumerate(answers):
        score[0]+=s1[idx%l1]==i #boolean 값을 더함으로써 if문을 대신함
        score[1]+=s2[idx%l2]==i
        score[2]+=s3[idx%l3]==i
    return [idx+1 for idx,i in enumerate(score) if i==max(score)]

#sol2
def solution(answers): #정답
    l=len(answers) #정답의 길이
    s=[list(range(1,6)),[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]] #학생 1,2,3이 찍는 패턴
    ans=[]
    mx=0 #최고점
    for i in range(3):
        t=s[i]*(l//len(s[i])+1)
        score=sum(1 for i in range(l) if t[i]==answers[i])
        if mx<score: #최고점 처리
            mx=score
            ans=[i+1]
        elif mx==score:
            ans+=[i+1]
        else:
            pass
    return ans

'''
#sol1
평균 실행 시간 : 1.3 평균 메모리 사용량: 10.21
#sol2
평균 실행 시간 : 0.89 평균 메모리 사용량: 10.29

sol1에서는 나머지를 이용하여 패턴을 반복하는 것을 구현했고, sol2에서는 실제로 answers의 길이만큼 패턴을 반복해주었다
최고점자도 sol1에서는 점수 리스트에서 max값과 같은 요소를 반환했다면 sol2에서는 ans 리스트에 최고점을 기록한 학생을 저장하는 방법을 사용했다
또 sol1은 바깥의 for문이 answers이고 sol2는 바깥의 for문이 학생이다
'''