#sol
def solution(keymap, targets): #할당된 문자열 배열, 입력하려는 문자열 배열
    key_dict=dict()
    ans=[]
    for k in keymap: #키별 할당된 최솟값 딕셔너리
        for idx, i in enumerate(k):
            if i not in key_dict:
                key_dict[i]=idx + 1
            else:
                key_dict[i]=min(key_dict[i], idx + 1)
    for t in targets: #타겟 단어 각 알파벳 key_dict에서 찾아서 합산
        tmp=[key_dict.get(x,-1) for x in t]
        if -1 in tmp:
            ans.append(-1)
        else:
            ans.append(sum(tmp))
    return ans

#sol1
def solution(keymap, targets): #할당된 문자열 배열, 입력하려는 문자열 배열
    key_dict=dict()
    ans=[]
    for k in keymap: #키별 할당된 최솟값 딕셔너리
        for idx,i in enumerate(k):
            if i not in key_dict:
                key_dict[i]=idx+1
            else:
                key_dict[i]=min(key_dict[i],idx+1)
    for t in targets: #타겟 단어 각 알파벳 key_dict에서 찾아서 합산
        cnt=0
        for k in t:
            tmp=key_dict.get(k,-1)
            if tmp==-1:
                cnt=-1
                break
            else:
                cnt+=tmp
        ans.append(cnt)
    return ans

'''
#sol
평균 실행 시간 : 0.68 평균 메모리 사용량: 10.14
#sol1
평균 실행 시간 : 0.55 평균 메모리 사용량: 10.2

두 코드는 같은 코드이지만
sol의 경우 키 딕셔너리에 없는 값이 나와 -1을 반환해야 해도 단어 끝까지 순회해서 sol1에서는 그 부분만 수정
'''