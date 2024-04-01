def di(li):
    h,v=set(),set() #가로 칸과 세로 칸의 집합
    if "".join(li).count("O")!=8: #룩의 개수가 8개가 아니라면 "no" 반환
        return "no"
    for i, j in enumerate(li): #체스판을 한 행씩 가져오고
        if j.count("O")==1: #해당 칸에 룩이 하나 있으면 가로/세로 집합에 해당 인덱스를 추가
            h.add(i)
            v.add(j.index("O"))
        else: #룩이 없거나 2개 이상이면 "no" 반환
            return "no"
    if len(h)==8 and len(v)==8: #가로/세로 칸의 길이가 8이라면 "yes" 반환
        return "yes"
    else: #아니라면 "no" 반환
        return "no"

ans=[] #한 번에 출력하기 위한 리스트
T=int(input()) #tc 개수
for t in range(1,T+1):
    li=[""]*8 #체스판 초기화
    for i in range(8):
        li[i]=input()
    res=di(li)
    ans.append(f"#{t} {res}")
for a in ans:
    print(a)

'''
가로 집합은 사실 필요 없었을 것 같아서 그 부분을 빼고도 제출해 봤는데
코드 길이 빼고는 별 차이 없어서 그대로 두기로 

제출일 기준 python 실행시간 1위, 메모리 1위
'''