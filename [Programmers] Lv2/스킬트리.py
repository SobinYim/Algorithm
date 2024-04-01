def solution(skill, skill_trees): #선행 스킬 순서, 유저들이 만든 스킬 트리
    ans=0
    for sk in skill_trees:
        if (tmp:="".join([i for i in sk if i in skill])) and not skill.startswith(tmp): #선행 스킬의 스킬만 남긴 tmp가 존재하나 선행 스킬 순서와 다르다면
            continue
        else:
            ans+=1
    return ans

'''
평균 실행 시간 : 0.01 평균 메모리 사용량: 10.22
'''