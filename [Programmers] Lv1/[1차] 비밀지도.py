def solution(n, arr1, arr2): #지도 1, 지도 2
    ans=[]
    for i,j in zip(arr1,arr2):
        m=bin(i|j)[2:].replace("1","#").replace("0"," ") #or 연산으로 지도 1,2 모두 비어있는 공간 탐색한 것을 기호로 해독
        ans.append((n-len(m))*" "+m) #길이 맞춰서 배열에 추가
    return ans

'''
평균 실행 시간 : 0.011 평균 메모리 사용량: 10.313

이 풀이에서는 n과 길이의 차로 길이를 맞춰줬다
미처 rjust나 zfill 생각을 못 했는데 다른 사람의 풀이에서 보고 오! 하는 생각이 들었다
기억해 둬야지,,, zfill은 길이 width까지 왼쪽부터 0으로 채우고 rjust/ljust는 방향에 따라 지정한 문자로 채운다
zfill을 쓸 거면 m=bin(i|j)[2:].zfill(n).replace("1","#").replace("0"," ")로 썼을 것이고
rjust를 쓸 거면 ans.append(m.rjust(n," "))로 썼을 것 같다
테스트 케이스가 오래 걸리는 케이스들이 아니라 속도는 거기서 거기다
대신 코드가 훨씬 보기 좋아지니까,,
'''