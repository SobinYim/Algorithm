#sol1
def solution(sizes): #명함의 크기
    mx,mn=[],[]
    for i in sizes:
        i.sort()
        mx.append(i.pop(-1))
        mn.append(*i)
    answer=max(mx)*max(mn)
    return answer

#sol2
def solution(sizes): #명함의 크기
    mx,mn=[],[]
    for i,j in sizes:
        mx+=[max(i,j)]
        mn+=[min(i,j)]
    answer=max(mx)*max(mn)
    return answer
'''
#sol1
평균 실행 시간 : 0.67 평균 메모리 사용량: 10.49
#sol2
평균 실행 시간 : 1.17 평균 메모리 사용량: 10.5

list 요소가 가로, 세로로 두 개뿐이라 정렬이 빠를 거라고 생각해서 sol1을 짰다
sol2는 max와 min 연산을 모두 해야 하는 반면, sol1은 정렬 후 pop으로 값을 가져오고 mn은 언패킹으로 처리
거기에 append를 사용해서 속도를 미세하게나마 더 올렸다
'''