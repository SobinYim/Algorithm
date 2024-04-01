#sol1
def solution(numbers, target): #양의 정수 배열, 타겟 넘버
    stack=[(n:=numbers.pop()),-n] #numbers의 수를 더하고 빼서 만든 수
    for i in numbers:
        tmp=[]
        for j in stack:
            tmp+=[j+i,j-i]
        stack=tmp
    return stack.count(target)

#sol2
from itertools import product
def solution(numbers, target): #양의 정수 배열, 타겟 넘버
    ans=0
    sign=product([1, -1], repeat=len(numbers)) #모든 경우의 수 부호
    for s in sign:
        n=0
        for i,j in zip(s,numbers):
            n+=i*j
        if n==target:
            ans+=1
    return ans

'''
#sol1
평균 실행 시간 : 38.93 평균 메모리 사용량: 20.21
#sol2
평균 실행 시간 : 408.86 평균 메모리 사용량: 10.08

sol1은 numbers를 순회하며 스택 안의 수에 +n,-n을 더한 후, tmp 리스트에 추가한다
stack을 순회한 후, n까지의 수를 덧뺄셈 하여 만든 tmp를 stack에 할당한다
이렇게 만든 리스트에서 타겟 넘버를 찾아 반환한다
sol2는 처음에 sum과 map을 이용해 짰는데 sum이 있어서 그런지 지금 코드의 시간이 두 배가량 걸렸다
모든 부호의 경우의 수와 numbers를 zip한 것을 순회하며 둘의 곱셈을 더하여준다
이 값이 target과 같으면 answer+1
sol2가 좀 느리긴 하다,,
 
아래는 다른 사람의 풀이에서 본 인상깊었던 풀이
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
평균 실행 시간 : 76.76 평균 메모리 사용량: 16.3
product로 푼 것은 같은데 훨씬 효율적이다
나는 모든 부호의 경우의 수를 구했다면 이 코드는 +n,-n 중 하나를 선택한 것의 합을 구하여 numbers의 수를 더하고 빼서 만든 수를 만들었다
코드도 짧고 쉽고 성능도 좋다

def dfs(nums, i, n, t):
    ret = 0
    if i==len(nums):
        if n==t: return 1
        else: return 0
    ret+=dfs(nums, i+1, n+nums[i], t)
    ret+=dfs(nums, i+1, n-nums[i], t)
    return ret
def solution(numbers, target):
    answer = dfs(numbers, 0, 0, target)
    return answer
평균 실행 시간 : 97.08 평균 메모리 사용량: 10.16
정석 dfs 풀이.. 아주 깔끔하다
'''