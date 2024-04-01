def solution(files): #파일명 배열
    for i,tg in enumerate(files):
        flag=False
        for j in range(len(tg)):
            if (tmp:=tg[j].isnumeric()): #파일명의 j번째 글자가 숫자라면(number)
                flag=True
            elif flag and not tmp: #파일명의 j-1번째 글자가 숫자이고 j번째 글자가 숫자가 아니라면(==tail)
                break
            else: #파일명 ~j번째 글자에 숫자가 나오지 않았다면(==head)
                start=j+1 #number 시작 인덱스는 적어도 j+1
        else:
            j+=1 #break 없이 파일명 끝까지 도달
        files[i]=[tg[:start],tg[start:j],tg[j:],i] #head,number,tail,idx(들어온 순서)
    files=sorted(files,key=lambda x:(x[0].lower(),int(x[1][:5]),x[-1])) #정렬
    return list(map(lambda x:"".join(x[:3]),files))

'''
평균 실행 시간 : 2.24 평균 메모리 사용량: 10.79

정렬 시 idx는 없어도 결과가 잘 반환되었으나 명시적으로 넣어주었다

아래는 마음에 들었던 풀이
import re
def solution(files):
    def key_function(fn):
        head,number,tail = re.match(r'([a-z-. ]+)(\d{,5})(.*)',fn).groups()
        return [head,int(number)]
    return sorted(files, key = lambda x: key_function(x.lower()))
정렬 key function에 정규식을 이용한 풀이!
key function과 정규식을 이용하는 풀이는 이 밖에도 몇 개 있었지만 위 코드랑 실행 시간에서 크게 차이 나지 않았다...
이 코드는 이해도 쉽고 group을 이용하여 매치를 여러 번 하지 않고 딱 필요한 부분만 컴팩트하게 사용한다는 점이 아주 마음에 든다! 평균 실행 시간 1.88ms
'''