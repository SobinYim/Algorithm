#sol1
def solution(babbling): #옹알이
    answer=0
    for i in babbling:
        for j in ["aya", "ye", "woo", "ma"]:
            if j*2 not in i: #연속 처리
                i=i.replace(j," ")
            else:
                break
        if not i.strip(): #replace를 마친 i가 공백만으로 이루어져 있다면
            answer+=1
    return answer

#sol2
def solution(babbling): #옹알이
    possible=["aya", "ye", "woo", "ma"]
    pp_dict={"a":3,"y":2,"w":3,"m":2} #시작 알파벳 별 옹알이 글자 수 딕셔너리
    answer=0
    for i in babbling:
        sub=0
        tmp="" #옹알이를 이루는 단어들의 첫 글자 인덱스
        while True:
            try:
                if i[sub] in pp_dict.keys() and i[sub:sub+pp_dict[i[sub]]] in possible: #옹알이 첫 글자가 사전 안에 있고 슬라이싱 한 값이 possible 안에 있는지
                    if tmp==i[sub:sub+pp_dict[i[sub]]]: #연속 처리
                        break
                    tmp=i[sub:sub+pp_dict[i[sub]]] #인덱스 재설정
                    sub+=pp_dict[i[sub]]
                else:
                    break
            except IndexError as e: #마지막에 일어나는 예외 처리
                break
            if sub==len(i):
                answer+=1
                break
    return answer

#sol3
def solution(babbling): #옹알이
    possible=list(map(list,["aya", "ye", "woo", "ma"])) #리스트로 변환
    answer=0
    for i in babbling:
        stack,prev=[],-1
        for j in i:
            stack+=[j] #철자 추가, 발음할 수 있는 옹알이라면 stack을 비운다
            if stack in possible:
                if possible.index(stack)==prev: #불가능한 경우
                    break
                prev=possible.index(stack)
                stack=[]
        if not stack:
            answer+=1
    return answer

'''
#sol1
평균 실행 시간 : 0.04 평균 메모리 사용량: 10.23
#sol2
평균 실행 시간 : 0.07 평균 메모리 사용량: 10.16
#sol3
평균 실행 시간 : 0.09 평균 메모리 사용량: 10.19

sol2>sol1>sol3 순으로 짰다
sol2가 예외 처리도 해야하고 복잡해서 마음에 안 들어서 짠 sol1
빠르고 심플하고 강력하다!
sol3은 그냥 다른 방법으로도 할 수 있을 것 같아서 짜 봤는데 평균 실행 시간은 제일 느렸다
for문으로 babbling의 철자 하나씩 가져오고 이를 또 할당하고, 가능한 옹알이 목록에 검사하고,, 느릴만 한 것 같다
'''