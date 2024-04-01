#sol1
def solution(s, n): #문자열, 밀어낼 거리
    ans=""
    abc_dict=dict((i, chr(i)) for i in range(65, 91)) #ord:chr a-zA-Z 딕셔너리
    abc_dict.update(dict((i, chr(i)) for i in range(97, 123)))
    for i in s:
        tmp=ord(i)+n #밀어낸 후의 ord 값
        if (i.islower() and tmp > 122) or (i.isupper() and tmp > 90): #범위를 넘어가면 -26
            tmp-=26
        ans+=abc_dict.get(tmp," ") #딕셔너리에 없다면 공백이므로 default는 공백으로 get
    return ans

#sol2
def solution(s, n): #문자열, 밀어낼 거리
    abc=list(map(chr,range(ord("a"),ord("z")+1)))*2 #알파벳을 이어붙여서 범위 바깥으로 나갔을 때 처리해줄 필요가 없도록
    answer=""
    for i in s:
        if i==" ": #공백은 리스트에 없으므로
            answer+=" "
            continue
        t=abc[abc.index(i.lower())+n] #알파벳 리스트의 인덱스를 가져온 후 n만큼 밀어준다
        if i.isupper(): #대문자 처리
            answer+=t.upper()
        else:
            answer+=t
    return answer
'''
#sol1
평균 실행 시간 : 0.18 평균 메모리 사용량: 10.22
#sol2
평균 실행 시간 : 0.23 평균 메모리 사용량: 10.18

sol1은 딕셔너리를 사용했고, sol2는 리스트를 사용했다
대문자(혹은 소문자)를 sol1에서는 딕셔너리에 대소문자를 모두 넣어서 해결했고, sol2에서는 둘 중 하나로 리스트를 만든 후, upper()를 사용해서 바꿔줬다

문자도 등호 연산이 된다는 걸 알았다! 비단 a-z A-Z만 되는 게 아니라 ord 값이 기준이라 특수문자도 들어간다 굿
'''