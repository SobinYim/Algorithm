#sol1
from itertools import combinations
def solution(nums): #숫자 배열
    answer=0
    plen=max(nums)*3 #최댓값 지정
    #plen=sum(sorted(nums, reverse=True)[:3])+2
    p=[0]*plen #에라토스테네스의 체
    for i in range(2,len(p)):
        if p[i]==1:
            continue
        else:
            for j in range(i*i,plen,i):
                p[j]=1
    for i in combinations(nums,3): #조합
        if p[sum(i)]==0: #수의 합이 소수일 때
            answer+=1
    return answer

#sol2
def solution(nums): #숫자 배열
    answer=0
    plen=max(nums)*3 #최댓값 지정
    p=[0]*plen #에라토스테네스의 체
    for i in range(2,len(p)):
        if p[i]==1:
            continue
        else:
            for j in range(i*i,plen,i):
                p[j]=1
    for i in range(len(nums)): #조합
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if p[nums[i]+nums[j]+nums[k]]==0: #수의 합이 소수일 때
                    answer+=1
    return answer

'''
#sol1
평균 실행 시간 : 1.82 평균 메모리 사용량: 10.16
#sol2
평균 실행 시간 : 1.41 평균 메모리 사용량: 10.2

소수 문제에는 어김없이 에라토스테네스의 체... 하도 많이 써서 외워버렸다
sol1와 sol2는 조합 구현 부분만 다르고 동일하다

최댓값 지정해주는 방법으로는 두 가지를 썼는데
1) plen=max(nums)*3
2) plen=sum(sorted(nums, reverse=True)[:3])

1은 nums의 길이가 길수록 이점을 갖고
2는 nums의 숫자 범위가 좁을수록 이점을 갖는다
데이터에 따라 다르게 쓸 수 있겠다
테스트 케이스에서는 큰 차이 없었다
'''