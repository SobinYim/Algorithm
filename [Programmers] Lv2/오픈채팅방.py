def solution(record): #기록
    nickname=dict() #유저 ID:닉네임 딕셔너리
    ans=[]
    record.reverse()
    for r in record:
        bh,*user=r.split() #행동, (유저ID, 닉네임)
        if (user[0] not in nickname.keys()) and len(user)==2: #유저 ID가 딕셔너리에 없고 user 길이가 2 이상일 때
            nickname[user[0]]=user[1]
    for r in record:
        bh,*user=r.split()
        if bh!="Change": #bh가 ["Enter","Leave"] 중 하나일 때
            ans.append(f"{nickname[user[0]]}님이 {'들어왔습니다' if bh=='Enter' else '나갔습니다'}.")
    return ans[::-1]

'''
평균 실행 시간 : 32.78 평균 메모리 사용량: 17.88

for문이랑 bh,*user=r.split() 부분이 두 번 나와서 신경 쓰이긴 하지만 뭐 어떻게 바꿔야 할지 몰라서 그냥 두기로,,
'''