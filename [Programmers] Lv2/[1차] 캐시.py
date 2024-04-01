def solution(cacheSize, cities): #캐시 크기, 도시 이름 배열
    if cacheSize==0: #캐시가 할당되지 않았을 때
        return len(cities)*5
    t=0 #실행 시간
    cities=list(map(lambda x:x.lower(),cities)) #소문자 통일
    cache=[[0]]*cacheSize #캐시
    for i in cities:
        if i in cache: #i를 최신 페이지로
            t+=1
            cache.remove(i)
            cache.append(i)
        else: #가장 오래된 페이지 제거, i 추가
            t+=5
            cache.pop(0)
            cache.append(i)
    return t

'''
평균 실행 시간 : 3.81 평균 메모리 사용량: 10.83

pop(0) 때문에 비효율적일 것 같아서 deque도 써봤는데 더 오래걸렸다 왜일까
'''