'''
1541. 거꾸로 출력해보아요
'''
li=list(range(int(input())+1))[::-1]
for i in li:
    print(i, end=" ")


'''
1933. 간단한 N 의 약수
'''
num = int(input())
li = []
for i in range(1,num):
    if i in li:
        break
    if i not in li and num%i==0:
        li.append(i)
        li.append(num//i)
for i in sorted(li):
    print(i,end=" ")


'''
1936. 1대1 가위바위보
'''
a,b=map(int,input().split())
num=a-b
if num==2 or num<0:
    print("B")
else:
    print("A")


'''
1938. 아주 간단한 계산기
'''
num=list(map(int, input().split()))
print(sum(num))
print(num[0]-num[1])
print(num[0]*num[1])
print(num[0]//num[1])


'''
2019. 더블더블
'''
num=int(input())
for i in range(num+1):
    print(2**i,end=" ")


'''
2025. N줄덧셈
'''
num=int(input())
print((1+num)*num/2)


'''
2027. 대각선 출력하기
'''
num=5
for i in range(num):
    for j in range(num):
        if i==j:
            print("#",end="")
        else:
            print("+",end="")
    print()


'''
2029. 몫과 나머지 출력하기
'''
T =int(input())
for i in range(T):
    num1, num2 = map(int, input().split(" "))
    print(f"#{i+1} {num1 // num2} {num1 % num2}")


'''
2043. 서랍의 비밀번호
'''
password,start_num=map(int,input().split())
print(password-start_num+1)


'''
2046. 스탬프 찍기
'''
print("#"*int(input()))


'''
2047. 신문 헤드라인
'''
head_line=input()
print(head_line.upper())


'''
2050. 알파벳을 숫자로 변환
'''
t=input().upper()
li=[i for i in t]
for i in li:
    print(ord(i)-64,end=" ")


'''
2056. 연월일 달력
'''
d_li = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
T = int(input())
for i in range(1, T + 1):
    date=input()
    y,m,d=date[:4],date[4:6],date[6:]
    if 0<int(m)<13 and 0<int(d)<=d_li[int(m)-1]:
         res=y+"/"+m+"/"+d
    else:
        res=-1
    print(f"#{i}",res)


'''
2058. 자릿수 더하기
'''
print(sum(map(int,input())))


'''
2063. 중간값 찾기
'''
n=int(input())//2
li=sorted(list(map(int,input().split())))
print(li[n])


'''
2068. 최대수 구하기
'''
T=int(input())
for i in range(T):
    res=max(map(int,input().split()))
    print(f"#{i+1} {res}")


'''
2070. 큰 놈, 작은 놈, 같은 놈
'''
T = int(input())
for i in range(1, T+1):
    n1,n2=map(int,input().split())
    res="<" if n1<n2 else "=" if n1==n2 else ">"
    print(f"#{i}",res)


'''
2071. 평균값 구하기
'''
T = int(input())
for i in range(1, T + 1):
    li=list(map(int,input().split()))
    print(f"#{i}",round(sum(li)/len(li)))


'''
2072. 홀수만 더하기
'''
T = int(input())
for i in range(1, T + 1):
    li=list(map(int,input().split()))
    odd=[i for i in li if i % 2 ==1]
    print(f"#{i}",sum(odd))