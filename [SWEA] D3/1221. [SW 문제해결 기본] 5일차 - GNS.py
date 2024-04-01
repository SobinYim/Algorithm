#sol1
num=["ZRO ","ONE ","TWO ","THR ","FOR ","FIV ","SIX ","SVN ","EGT ","NIN "] #숫자 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    _=input()
    s=input()+" " #문자열, num 리스트에 공백이 포함된 형태로 들어가 있기 때문에 뒤에 공백을 추가해 줌
    res="" #res 초기화
    for i in num: #num 리스트를 돌며 i의 개수만큼 res에 붙여넣어줌, num이 순서대로 들어가 있기 때문에 정렬되어 출력
        res+=(i)*s.count(i)
    print(f"#{t}\n",res)

#sol2
num_d={"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9} #숫자-문자 dict
T=int(input()) #tc 개수
for t in range(1,T+1):
    _=input()
    li=input().split() #공백을 기준으로 split
    res=" ".join(sorted(li,key=lambda x: num_d[x])) #num_d를 이용해 문자를 숫자로 변환한 결과를 키 값으로 정렬, join을 이용해 붙임
    print(f"#{t}\n",res)

'''
단어가 많이 들어오다 보니 정렬에 시간이 걸려 sol1이 sol2보다 훨씬 효율적이었음
'''