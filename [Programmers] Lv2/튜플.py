def solution(s): #튜플을 표현하는 부분 집합
    answer=[] #튜플
    string=sorted(s[2:-2].split("},{"),key=lambda x: len(x)) #튜플의 부분 집합을 구분하는 "},{"를 구분자로 나누고, 길이 순으로 정렬
    for i in string:
        answer+=set(map(int,i.split(","))).difference(answer) #int형으로 변환 후, answer과 차집합한 결과(==새로운 요소)를 추가
    return answer

'''
평균 실행 시간 : 9.2 평균 메모리 사용량: 10.82

튜플의 부분 집합들을 길이 순으로 정렬하고 이전 집합에 없었던 요소를 추가하면 튜플이 뭔지 알 수 있다

import re
from collections import Counter
def solution(s):
    c=Counter(re.findall('\d+', s))
    return [int(k) for k, v in sorted(c.items(), key=lambda x: x[1], reverse=True)]
평균 실행 시간 : 12.4 평균 메모리 사용량: 13.51
이 풀이는 빈도 순으로 요소를 반환하여 튜플을 찾아낸다
접근법도 좋고 코드 심플하고 속도도 빨라서 마음에 든다 
'''