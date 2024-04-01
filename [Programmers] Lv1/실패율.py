#sol1
from itertools import accumulate
from collections import Counter
def solution(N, stages): #스테이지 수, 유저들이 도달한 스테이지
    user=len(stages)
    stage=[0]*(N+1) #각 스테이지에 도달한 유저
    for idx,cnt in Counter(stages).items():
        stage[idx-1]=cnt
    accum=list(accumulate([0]+stage))[:-1] #각 스테이지를 거쳐간 유저 수
    fr=[] #실패율
    for i in range(0,N):
        if user==accum[i]: #해당 스테이지을 거쳐간 유저 수와 전체 유저 수가 같다면
            fr.append([0,i+1]) #(실패율, 인덱스)
        else:
            fr.append([stage[i]/(user-accum[i]),i+1])
    fr.sort(key=lambda x: x[0],reverse=True) #실패율을 키 값으로 정렬
    answer=[i[1] for i in fr]
    return answer

#sol2
from collections import Counter
def solution(N, stages): #스테이지 수, 유저들이 도달한 스테이지
    fr=dict((i,0) for i in range(1,N+2)) #실패율
    c=sorted(Counter(stages).items(),reverse=True) #각 스테이지에 도달한 유저
    idx,accum=c.pop(0) #유저가 도달한 최대 스테이지, 해당 스테이지에 도달한 유저 수
    fr[idx]=1
    for idx,cnt in c:
        accum+=cnt #누적
        fr[idx]=(cnt/accum) #실패율
    fr.pop(N+1)
    return [k for k,v in sorted(fr.items(),key=lambda x:(x[1],-x[0]),reverse=True)] #실패율을 키 값으로 정렬

'''
#sol1
평균 실행 시간 : 3.96 평균 메모리 사용량: 11.26
#sol2
평균 실행 시간 : 4.16 평균 메모리 사용량: 11.27

sol1은 누적 리스트를 만들어서 1부터 N까지 순회를 한다면
sol2는 카운터를 순회하며 누적을 쌓고 실패율을 계산해 딕셔너리에 넣는다
딕셔너리를 사용해 미리 값을 넣어놔서 모든 스테이지를 계산할 필요가 없다
그래서 sol2가 더 빠를 줄 알았는데 의외로 sol1이 빨랐다,,
그래도 sol2쪽이 더 마음에 든다!
'''