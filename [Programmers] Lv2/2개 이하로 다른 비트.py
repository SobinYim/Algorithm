def solution(numbers): #정수 배열
    ans=[]
    for i in numbers:
        b=bin(i)[2:] #2진수 변환
        idx=len(b)-b.rfind("0")-2 #오른쪽부터 세었을 때 가장 가까운 0의 위치-1(==1 위치)
        if idx<0:
            idx=0
        ans.append(i+2**idx)
    return ans

'''
평균 실행 시간 : 30.78 평균 메모리 사용량: 17.7

idx=max(len(b)-b.rfind("0")-2,0)를 해도 되는데 속도가 살짝 느려져서 if문으로 돌려놨다

아래는 비트 연산을 이용한 풀이
[((n ^ (n+1)) >> 2)+n+1 for n in numbers]
평균 실행 시간 : 13.23 평균 메모리 사용량: 17.69
n+2**x 라는 면에서 같지만 비트 연산 쪽이 역시 깔끔하다,,,
'''