m={"b":"d","d":"b","p":"q","q":"p"} #거울상
T=int(input()) #tc 개수
for t in range(1,T+1):
    res="".join(map(lambda x: m[x],input()[::-1])) #input 받은 값을 뒤집은 것을 dict m의 값으로 대체 후 join
    print(f"#{t}",res)

'''
제출일 기준 python 실행시간 14위, 코드길이 3위  
'''