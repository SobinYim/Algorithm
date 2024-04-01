T=int(input()) #tc 개수
for t in range(1,T+1):
    n=int(input()) #문장의 개수
    s=input() #문장
    s=(s+" ").replace("! ",". ").replace("? ",". ").rstrip(". ").split(". ") #구두점 정리, 구두점을 기준으로 split
    res=[0]*n
    for i,j in enumerate(s):
        res[i]=sum(map(lambda x: 1 if x.istitle()==True and x.isalpha()==True else 0,j.split())) #첫 글자가 대문자이고 나머지가 소문자로만 이루어진 단어 카운트
    print(f"#{t}",*res)

'''
정리하면서 다시 풀어보려고 했는데,,, 뭐가 바뀌었는지 runtime error만 뜨고 pass가 도저히 안 남,,, <풀이중> 엔딩,,
위 코드는 해당 문제가 없었을 때 pass 났던 코드,,,,
'''