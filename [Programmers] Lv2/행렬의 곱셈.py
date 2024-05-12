#sol1
def solution(arr1, arr2): #행렬1, 행렬2
    arr2=list(zip(*arr2)) #전치
    ans=[]
    for i in arr1:
        tmp=[]
        for j in arr2:
            tmp.append(sum(map(lambda x,y:x*y,i,j)))
        ans.append(tmp)
    return ans

#sol2
def solution(arr1, arr2): #행렬1, 행렬2
    arr2=list(zip(*arr2)) #전치
    ans=[[0]*len(arr2) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            tmp=0
            for a,b in zip(arr1[i],arr2[j]):
                tmp+=(a*b)
            ans[i][j]=tmp
    return ans

'''
sol1
평균 실행 시간 : 17.44 평균 메모리 사용량: 10.54
sol2
평균 실행 시간 : 14.81 평균 메모리 사용량: 10.54

행-열 계산이 번거로워서 행-행 계산으로 바꾸기 위해 arr2를 전치했다
sol1은 행 계산을 마친 후 ans 행렬에 추가하는 방법이고
sol2는 ans 행렬을 미리 만들어 놓은 후, 값을 채워줬다
또 계산 방법 구현도 살짝 다른데 계산은 map을 사용하여 구현한 반면, sol2는 for문을 이용하여 계산했다

import numpy as np
def solution(arr1, arr2):
    return (np.matrix(arr1)*np.matrix(arr2)).tolist()
평균 실행 시간 : 0.87 평균 메모리 사용량: 28.65
numpy를 이용한 풀이!
물론 정석 풀이는 아니겠지만 실행 시간이 인상적이다
'''