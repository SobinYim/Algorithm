def solution(n, words): #게임 참가자 수, 단어 배열
    use=[words.pop(0)] #첫 단어
    r=1 #턴
    for i in words:
        if i not in use and i[0]==use[-1][-1]: #사용하지 않은 단어이고 직전 단어의 끝 글자와 현재 단어의 첫 글자 일치
            use+=[i]
            r+=1
        else:
            return [r%n+1,r//n+1] #나머지로 탈락자를 구하고 몫으로 몇 번째 차례였는지(0부터 시작해서 +1씩)
    return [0,0]

'''
평균 실행 시간 : 0.016 평균 메모리 사용량: 10.23
'''