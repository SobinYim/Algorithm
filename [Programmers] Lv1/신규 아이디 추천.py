#sol1
def solution(new_id): #입력된 아이디
    ans=[i for i in new_id.lower() if i.isalnum() or i in "._-"] #~step2
    stack=[]
    for i in ans: #step3
        if stack and stack[-1]==i==".":
            continue
        stack.append(i)
    ans="".join(stack).strip(".")[:15].rstrip(".") #step4,6
    if (l:=len(ans))<3: #step5,7
        if not ans:
            ans="aaa"
        else:
            ans+=ans[-1]*(3-l)
    return ans

#sol2
import re
def solution(new_id): #입력된 아이디
    ans=re.sub(r"[^a-z0-9_.-]","",new_id.lower()) #~step2
    ans=re.sub("\.+",".",ans).strip(".")[:15].rstrip(".") #step3,4,6
    if (l:=len(ans))<3: #step5,7
        if not ans:
            ans="aaa"
        else:
            ans+=ans[-1]*(3-l)
    return ans

'''
#sol1
평균 실행 시간 : 0.06 평균 메모리 사용량: 10.24
#sol2
평균 실행 시간 : 0.16 평균 메모리 사용량: 10.21

sol2>sol1 순서로 짰다
다른 사람의 풀이 댓글로 모듈 없이 구현하는 게 맞지 않냐는 말 보고 그런가? 하고 짜봤다,,
의외로 re 모듈을 사용하는 것보다 속도가 빨랐다

다른 사람의 풀이에서 ans.ljust(3, ans[-1]) 보고 아차 했다,,
맨날 보면 생각나는데 풀 때는 꼭 생각이 안 난다,,
연속된 .문자 제거하는 코드! 
while ".." in ans:
    ans=ans.replace("..",".")
심플하고 빠르다!
'''