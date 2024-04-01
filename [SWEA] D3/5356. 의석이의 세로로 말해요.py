from itertools import zip_longest
T=int(input()) #tc 개수
for t in range(1,T+1):
    li=[] #문자열
    for i in range(5):
        li.append(input().replace(" ",""))
    res="".join(map("".join,zip_longest(*li,fillvalue="")))
    print(f"#{t}",res)

'''
zip_longest
전치행렬의 경우 zip 함수를 사용하여 만들 수 있음
위와 같이 길이가 다를 경우 최소길이를 기준으로 잘리기 때문에 최대 길이를 기준으로 하는 zip_longest를 사용
fillvalue 옵션을 이용하여 값이 없는 부분을 무엇으로 채울지 지정해 줄 수 있음

제출일 기준 python 코드길이 9위
'''