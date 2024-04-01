def solution(arr): #0과 1로 이루어진 2차원 정수 배열
    ans=[0]*2 #0,1 개수
    n=len(arr)
    def compress(n,arr):
        tmp=set()
        for i in arr:
            tmp.update(set(i))
        if len(tmp)==1: #현재 arr의 요소가 모두 동일하다면 ans 업데이트
            ans[tmp.pop()]+=1
        else: #아니라면 재귀
            n//=2
            compress(n,[i[:n] for i in arr[:n]]) #좌상
            compress(n,[i[n:] for i in arr[:n]]) #우상
            compress(n,[i[:n] for i in arr[n:]]) #좌하
            compress(n,[i[n:] for i in arr[n:]]) #우하
    compress(n,arr)
    return ans

'''
평균 실행 시간 : 55.04 평균 메모리 사용량: 13.14
'''