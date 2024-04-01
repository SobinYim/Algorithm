def solution(n): #자연수 n
    b=list("0"+bin(n)[2:]) #1111과 같은 경우에 대응하기 위해 이진수 변환한 값 앞에 "0"를 붙여준다
    pt=len(b) #시작 인덱스
    t="0" #비교를 위한 직전 요소
    for i in b[::-1]: #바꿔야 하는 부분==뒤에서 1이 등장한 후 다시 0이 나오는 그 위치(==숫자가 커져야 하므로)
        if t!=i and i=="0": #직전에 나온 요소와 현재 요소가 다르고 현재 요소가 0이라면 break
            break
        t=i
        pt-=1
    b[pt],b[pt-1]=b[pt-1],b[pt] #0과 그 뒤의 1 위치를 바꾸어서(Ex_0100110>0101010) 1의 개수가 같으면서 큰 수로 만들어 준다
    b[pt:]=sorted(b[pt:]) #해당 위치 이후로는 오름차순 정렬을 해주어서 조건을 지키면서 가장 작은 수로 만든다
    return int("".join(b),2) #이를 이은 후, 10진수로 변환

'''
[효율성  테스트] 평균 실행 시간 : 0.01 평균 메모리 사용량: 10.133

조건::
조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.

정직하게,, 정말 0과 1의 개수가 같으면서 큰 수,,, 그 중에서 가장 작은 수를 만들었다,,,,
풀고 나서는 살짝 뿌듯했는데,,,, 다른 풀이 보면서,,, 조금 눈물이 났다,,,,,,

미친 풀이..
def solution(n):
    pivot = n & -n;
    before = ((n ^ (n + pivot)) // pivot) >> 2;
    return (n + pivot) | before;

비트 연산 개고수.... 너무너무 멋있다...

n과 n의 보수를 &연산하여 가장 오른쪽 1 위치를 찾고
n+pivot으로 1 이전에 등장하는 0을 1로 바꿔준다
n+pivot하면 1의 개수가 줄어들므로 
이 값을 n과 xor 연산한 것(==없어진 1 개수(오른쪽에서 첫 번째로 나오는 1 더미들)+값이 커지며 바뀐 부분 1곳)을 
>>2 쉬프트하여 1의 개수를 맞추기 위한 값을 찾는다(값이 커지며 바뀌어야 하는 두 부분은 둬야 하니까 >>2)
n과 pivot을 더한 값(==큰 수 만들기)과 before을 or 연산(==1의 개수가 같도록 만들어주기)하면... 답이 나온다....

"위치 찾아서 바꿔주고 1 더미들을 뒤에 붙인다"는 면에서 내가 짠 코드와 같지만,,
세련되고 깔끔하고,,, 심플하고 성능 좋고,,, 진짜 완전 짱이다

def solution(n):
    b = bin(n)
    b0 = b.rstrip('0')
    b1 = b0.rstrip('1')
    chk0 = len(b) - len(b0)
    chk1 = len(b0) - len(b1)
    return n + 1 + int('0b0'+'1'*chk0, 2) + int('0b0'+'1'*(chk1-1), 2)
이건 조금 특이한데 비트를 조작하지 않고 int를 더해서 값을 만드는 게 인상 깊었다
b0는 뒤에서 연속으로 등장하는 0 제거한 값, b1은 그 다음에 연속으로 등장하는 1 제거한 값
chk0는 b0에서 제거한 0 개수, chk1은 b1에서 제거한 1 개수이다
1+int('0b0'+'1'*chk0, 2)로 1 더미 앞의 0을 올려주고 int('0b0'+'1'*(chk1-1), 2)로 1의 개수를 맞춰준다

#위 풀이 참고하여 일부 개선
def solution(n):
    b="0"+bin(n)[2:]
    b0=b.rstrip("0")
    b1=b0.rstrip("1") 
    n0=len(b)-len(b0)+1 #맨 뒤 0 개수
    n1=len(b0)-len(b1)-1 #그 뒤의 1 개수
    ans=b[:len(b1)-1]+"1"+"0"*n0+"1"*n1 # +"0" 부분 때문에 n0,n1에 +1,-1 씩 해주었다
    return int(ans,2)
[효율성  테스트] 평균 실행 시간 : 0.003 평균 메모리 사용량: 10.15
for문 대신 뒤의 0,1을 차례로 rstrip 한 길이로 그 다음 0의 인덱스를 구해주었고
정렬 대신 0*n0+1*n1으로 strip한 개수를 붙이는 것으로 대체했다!
변수가 좀 많은가 싶기도 하지만 .1ms 밑으로 내려가서 고무적!


def solution(n):
    i=1
    while True:
        if bin(n).count('1')==bin(n+i).count('1'):
            return n+i
        i+=1
이건 다른 풀이에서 많이 나온 로직,,,
n에 1씩 더하면서 "1"의 개수가 같은지 검사해서 같다면 해당 값 return
while True에 n 이상의 모든 수를 검사해서 느릴 거라고 생각했는데 효율성 테스트 값도 아주 좋았다...
심플하면서 성능도 좋은 인상 깊은 풀이!
bin(n).count('1')을 따로 저장해두면 더 빨라질 것 같다
'''