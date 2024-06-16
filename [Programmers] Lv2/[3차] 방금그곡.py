def conv_melody(melody): #멜로디 -> 반음을 소문자로 변환
    stack = []
    for i in melody:
        if i == "#":
            stack[-1] = stack[-1].lower()
        else:
            stack.append(i)
    return "".join(stack)
def cal_t(start, end): #시작 시간, 종료 시간 -> 음악이 재생된 시간 계산
    t = conv_min(end) - conv_min(start)
    return t
def conv_min(t): #시간 -> HH:MM 표기 시간을 분 단위로 변환
    hh, mm = map(int, t.split(":"))
    return hh * 60 + mm
def solution(m, musicinfos): #네오가 기억한 멜로디, 방송된 곡의 정보
    m = conv_melody(m)
    l = len(m)
    ans = "(None)"
    ans_t = -1
    musicinfos.sort(key=lambda x: x[:5]) #시작한 시각을 기준으로 정렬
    for i in musicinfos:
        start, end, music, melody = i.split(",") #시작한 시각, 끝난 시각, 음악 제목, 악보 정보
        if (playback_t := cal_t(start, end)) >= l: #음악이 재생된 시간이 기억하던 멜로디의 길이보다 길거나 같다면
            melody = conv_melody(melody)
            melody = (melody * (playback_t // len(melody) + 1))[:playback_t] #재생 시간에 맞추어 슬라이싱
            if m in melody and playback_t > ans_t: #기억하던 멜로디가 재생된 멜로디에 포함되어 있고, 저장된 재생된 시간보다 더 오래 재생되었다면
                ans = music
                ans_t = playback_t
    return ans


'''
평균 실행 시간 : 0.26 평균 메모리 사용량: 10.35

replace로 일일이 바꿔주기 싫어서 for문을 이용하여 처리했는데 아무래도 실행 시간에서 차이가 났다
(conv_melody를 replace로 바꿔줄 시 평균 실행 시간 : 0.13 평균 메모리 사용량: 10.39)
len(melody)를 쓰는데 멜로디를 먼저 바꾸지 않아서 살짝 헤맸다
여러모로 아쉬운 풀이
'''