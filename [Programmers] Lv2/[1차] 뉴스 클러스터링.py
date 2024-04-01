#sol1
from re import compile
from collections import Counter
def create_strset(string): #문자열에서 연속으로 등장하는 영문자를 찾고 Counter형으로 반환
    string=string.lower() #소문자 통일
    pattern=compile(r"(?=([a-z]{2}))") #소문자가 연속으로 등장하는 패턴
    return Counter(pattern.findall(string))

def solution(str1, str2): #문자열 1,2
    v1=create_strset(str1)
    v2=create_strset(str2)
    if uni:=v1|v2: #합집합이 존재할 경우
        return int((sum((v1&v2).values())/sum((uni).values()))*65536) #자카드 유사도
    return 65536 #존재하지 않을 경우 {}/{} == 1로 처리

#sol2
from collections import Counter
def solution(str1, str2): #문자열 1,2
    str1,str2=str1.lower(),str2.lower() #소문자 통일
    v1=Counter(k for i in range(len(str1)-1) if (k:=str1[i:i+2]).isalpha())
    v2=Counter(k for i in range(len(str2)-1) if (k:=str2[i:i+2]).isalpha())
    if uni:=v1|v2: #합집합이 존재할 경우
        return int((sum((v1&v2).values())/sum((uni).values()))*65536)
    return 65536 #존재하지 않을 경우 {}/{} == 1로 처리

'''
#sol1
평균 실행 시간 : 0.22 평균 메모리 사용량: 10.31
#sol2
평균 실행 시간 : 0.14 평균 메모리 사용량: 10.27

sol1은 정규식을 이용해 연속한 영문자를 찾았고, 이를 함수로 분리했다
r"(?=([a-z]{2}))"을 사용했는데 긍정형 전방탐색은 텍스트의 위치만 찾아내서 예를 들어 "code" 면 ["co","od","de"] 가 나오는 반면
전방탐색 없이 r"[a-z]{2}"를 사용하면 매치된, 이미 처리된 부분을 건너뛰어버린다.. 그래서 ["co","de"]가 나와버린다..

sol2는 for문을 이용해 문자열을 슬라이싱하고 str.isalpha()를 이용해 영문자만으로 이루어졌는지 검사했다

월러스 연산자를 손에 익혀두려고 사용해봤다!
특히 리스트 컴프리헨션에서 사용하니까 아주 편했다!
'''