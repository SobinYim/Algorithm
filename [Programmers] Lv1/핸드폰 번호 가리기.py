def solution(phone_number): #전화번호
    return "*"*(len(phone_number)-4)+phone_number[-4:] #뒷 4자리를 제외한 번호 마스킹

'''
평균 실행 시간 : 0.0 평균 메모리 사용량: 10.162

왜 lv0이 아닌지 모를 문제...
'''