def solution(s): #문자열
    return " ".join(map(lambda x: x.capitalize(),s.split(" ")))

'''
평균 실행 시간 : 0.01 평균 메모리 사용량: 10.21

str.capitalize() 만 알고 있다면 어렵지 않은 문제
공백 문자가 연속으로 등장할 수 있어서 split(" ")을 사용했다

지금은 조건이 바뀌어서 쓸 수 없지만 str.title()을 쓰면 더 쉽게 첫 글자만 대문자로 바꿀 수 있다!
capitalize는 단어 앞에 특수문자나 숫자가 오면 영문자의 첫 글자를 대문자로 바꾸지 않지만 title은 앞과 상관없이 대문자로 바꾼다
'''