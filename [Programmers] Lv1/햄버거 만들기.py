def solution(ingredient): #햄버거 재료
    ans=0
    ingr=[] #현재 쌓인 재료
    for i in range(len(ingredient)):
        tg=ingredient[i]
        if tg==1: #빵이라면 햄버거가 만들어지는지 검사
            if ingr[-3:]==[1,2,3]:
                del ingr[-3:]
                ans+=1
            else:
                ingr.append(1)
        else:
            ingr.append(tg)
    return ans

'''
평균 실행 시간 : 45.45 평균 메모리 사용량: 14.51

나는 del을 썼지만 pop을 3번 돌리는 것도 생각보다 빠르다는 걸 느꼈다
'''