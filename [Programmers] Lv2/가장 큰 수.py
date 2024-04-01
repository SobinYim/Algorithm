from functools import cmp_to_key
def solution(numbers): #0 또는 양의 정수가 담긴 배열
    def sort_fn(x,y): #x+y, y+x를 비교함으로써 대소 비교(x,y==str형으로 변환한 정수)
        if x+y<y+x:
            return 1
        else:
            return -1
    ans="".join(sorted(map(str,numbers),key=cmp_to_key(lambda x,y: sort_fn(x,y)))) #정렬한 결괏값을 "".join()으로 이어준다
    if ans[0]=="0":
        ans="0"
    return ans

'''
평균 실행 시간 : 92.71 평균 메모리 사용량: 13.28

정렬 key 중에서 아래 코드가 빨랐다
ans="".join(sorted(map(str,numbers),reverse=True,key=lambda x:(x*4).ljust(4)))
원본 풀이에서는 str(x)*4을 썼지만 이게 더 빠르다
4는 number의 원소 길이라 조건이 변한다면 코드를 수정해야하는 점이 걸리지만 빠르니까,,
실행 시간 차이가 상당히 크게 나는데 아마도 cmp_to_key 사용의 차이일 것 같다...
'''