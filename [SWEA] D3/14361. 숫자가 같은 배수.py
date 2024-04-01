T=int(input()) #tc 개수
for t in range(1,T+1):
    n=int(input()) #자연수 n
    li=sorted(str(n)) #n을 구성한 숫자들을 차례로 정렬
    res="impossible"
    for i in range(2,10): #n의 배수를 다시 정렬하여 정렬된 리스트 li와 같으면 "possible", break
        temp=str(n*i)
        if len(li)!=len(temp): #n과 n의 배수의 자릿수가 다르면 break
            pass
        elif sorted(temp)==li:
            res="possible"
        else:
            continue
        break
    print(f"#{t}",res)