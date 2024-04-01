#sol1
def solution(arr, divisor): #배열, 나눗수
    answer=sorted([i for i in arr if i%divisor==0]) #divisor로 나눠지는 수 리스트 정렬
    return answer if answer else [-1]

#sol2
def solution(arr, divisor): #배열, 나눗수
    answer=sorted(set(range(divisor,max(arr)+1,divisor))&set(arr)) #arr과 divisor의 배수의 교집합 정렬
    return answer if answer else [-1]

'''
#sol1
평균 실행 시간 : 0.3 평균 메모리 사용량: 10.44
#sol2
평균 실행 시간 : 2.84 평균 메모리 사용량: 12.37

sol1은 for문을 이용해 각 요소들을 divisor로 나눠주었다면 sol2는 divisor의 배수 집합을 만들어 arr와의 교집합을 구해주었다
그러다 보니까 range()를 또 set로 만들어주고 교집합 연산하고 이걸 또 정렬하다 보니 비효율적일 수밖에 없는 것 같다..
사실 정렬 안 쓰고 풀 수 있나 해서 set를 썼는데 생각해 보니 set에 순서가 없기도 하고 리스트 변환해도 입력 순이나 값 순으로 나오는 게 아니라 결국 정렬이 필요했다...
그래서 OrderedDict처럼 ordered set이 있나 검색하니 github엔 있었으나 프로그래머스 같은 클라우드 ide에서 사용은 어려울 것 같았다...
ㅠㅠ 
'''