#sol1
n,m = map(int, input().strip().split())
for _ in range(m):
    print("*"*n)

#sol2
n,m = map(int, input().strip().split())
print("\n".join(["*"*n]*m))

'''
#sol1
평균 실행 시간 : 13.59 평균 메모리 사용량: 7.53
#sol2
평균 실행 시간 : 18.03 평균 메모리 사용량: 7.58

왜 lv0이 아닌지 모를 문제...
무슨 풀이를 봐도 시간들이 많이 걸린다
SWEA에서도 느꼈지만 print가 진짜 의외로 시간 많이 먹는 것 같다
'''