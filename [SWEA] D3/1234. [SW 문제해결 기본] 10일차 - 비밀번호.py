li=[str(i)*2 for i in range(10)] #삭제할 문자열
for t in range(1,11):
    _,s=input().split() #문자열
    while True:
        for i in li: #삭제
            s=s.replace(i,"")
        if sum(list(map(lambda x:s.find(x),li)))==-10: #li의 문자열이 s에 없으면 break
            break
    print(f"#{t}",s)