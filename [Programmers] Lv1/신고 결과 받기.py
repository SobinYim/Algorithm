def solution(id_list, report, k): #ID 목록, 신고 정보, 정지 기준
    l=len(id_list)
    user_idx=dict([(j,i) for i,j in enumerate(id_list)]) #유저 id:인덱스 딕셔너리
    report_dict=dict([(i,set()) for i in id_list]) #신고인:피신고인 딕셔너리
    report_cnt=[0]*l #신고 누적 횟수
    for i in set(report): #중복 신고 제거
        uid,r=i.split() #신고인, 피신고인
        report_cnt[user_idx[r]]+=1
        report_dict[uid].add(r)
    banned=set([id_list[i] for i in range(l) if report_cnt[i]>=k]) #누적 횟수에 따라 정지된 유저
    if not banned:
        return [0]*l
    for i in report_dict.items():
        uid,r=i #신고인, 피신고인
        report_dict[uid]=len(r.intersection(banned)) #신고인이 신고한 유저와 정지된 유저의 교집합 == 결과 메일 수신 횟수
    return list(report_dict.values())

'''
평균 실행 시간 : 31.8 평균 메모리 사용량: 19.53

안 풀리면 나중에 다시 푸는 것도 방법 같다
'''