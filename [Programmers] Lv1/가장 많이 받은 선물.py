from collections import Counter,defaultdict
def solution(friends, gifts):
    c=Counter(gifts)
    gift_index=defaultdict(lambda: 0) #친구:선물 지수 딕셔너리
    receive_gift=defaultdict(lambda: 0) #친구:받을 선물 수 딕셔너리
    for k,v in c.items(): #선물 지수 계산(주면 +, 받으면 -)
        g,r=k.split() #준 사람, 받은 사람
        gift_index[g]+=v
        gift_index[r]-=v
    for i,f1 in enumerate(friends): #받을 선물 수 계산
        for j in range(i+1,len(friends)):
            f2=friends[j]
            f1_received=c.get(f"{f2} {f1}",0) #f1가 f2에게 받은 선물 수
            f2_received=c.get(f"{f1} {f2}",0) #f2가 f1에게 받은 선물 수
            if f1_received>f2_received:
                receive_gift[f2]+=1
            elif f1_received<f2_received:
                receive_gift[f1]+=1
            else: #같다면 선물 지수 비교
                if gift_index[f1]>gift_index[f2]:
                    receive_gift[f1]+=1
                elif gift_index[f1]<gift_index[f2]:
                    receive_gift[f2]+=1
    return max(receive_gift.values()) if receive_gift else 0

'''
평균 실행 시간 : 0.95 평균 메모리 사용량: 10.47

처음에는 선물 지수를
gift_index=defaultdict(lambda: [0,0]) #[준 선물, 받은 선물]
for k,v in c.items():
    g,r=k.split()
    gift_index[g][0]+=v
    gift_index[r][1]+=v
for k,v in gift_index.items():
    gift_index[k]=(lambda x,y: x-y)(*v)
gift_index.default_factory=lambda: 0
이렇게 냈었는데 default 값을 변경하는 부분이 마음에 안 들어서 보니
어차피 순회하면서 빼면서 왜 위에선 더하고 있지 하는 생각이 들어서 후다닥 바꿨다
정답률 보고 어려울 줄 알았는데 lv1은 lv1인지 무난했던 문제!

다른 사람의 풀이에 보니 Counter 없이 행렬로 푸는 방법도 있었다
'''