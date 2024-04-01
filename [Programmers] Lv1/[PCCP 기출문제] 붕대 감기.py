def solution(bandage, health, attacks): #[시전 시간, 초당 회복량, 추가 회복량], 최대 체력, [공격 시간, 피해량]
    mx_health=health #최대 체력 새로 할당
    tmp_t=0
    for t,damage in attacks:
        if not tmp_t:
            tmp_t=t
            health-=damage
        else:
            diff=t-tmp_t-1 #공격으로부터 지난 시간
            health=min(health+diff*bandage[1]+diff//bandage[0]*bandage[2],mx_health) #회복 후 체력
            health-=damage
            tmp_t=t
        if health<=0:
            return -1
    return health

'''
평균 실행 시간 : 0.01 평균 메모리 사용량: 10.19
'''