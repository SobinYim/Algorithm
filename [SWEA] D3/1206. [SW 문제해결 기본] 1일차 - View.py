for t in range(10):
    n=int(input()) #건물의 개수
    li=list(map(int,input().split())) #건물의 높이
    res=0 #결과값 초기화
    for i in range(n):
        temp=li[i]-max(*li[i-2:i],*li[i+1:i+3])
        res+=temp if temp>0 else 0
    print(f"#{t+1}",res)

'''
건물 높이 리스트의 요소를 순차로 돌며 i의 앞뒤 2개 요소를 언패킹하여 최댓값을 i에서 뺀 후,
이 값이 0보다 클 경우(==조망이 확보된 세대 수) 이 값을 res에 더하여 줌
'''