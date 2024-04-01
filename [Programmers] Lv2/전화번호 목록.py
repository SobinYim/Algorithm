def solution(phone_book): #전화번호 목록
    phone_book.sort() #정렬
    tmp=phone_book[0]
    for i in phone_book[1:]:
        if i.startswith(tmp): #전화번호가 이전 전화번호로 시작한다면
            return False
        else:
            tmp=i
    return True

'''
[효율성  테스트] 평균 실행 시간 : 41.17 평균 메모리 사용량: 20.05

정렬하면 알파벳순으로 정렬하되 길이가 짧은 게 앞으로 가는 것을 이용하여 풀었다
정렬 사용 시 시간 효율도가 떨어진다기에 더 빠른 풀이가 있을까 해서 앞뒤 세 페이지 정도 sort 없는 풀이들을 봤는데 이 코드보다 빠르지 않았다...
배열의 크기가 늘어날수록 오래 걸린다는 점은 동의해서,, 궁금한디... 더 찾아보기엔 시간이 조금 아까워서 넘어가기로! 아쉽다

아래는 hash를 이용해 푼 정석 풀이다!
def solution(phone_book):
    hash_map=dict((phone_number,1) for phone_number in phone_book)
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                return False
    return True
효율성 테스트 1,2는 hash를 이용한 풀이가 빨랐고, 효율성 테스트 3,4는 정렬을 이용한 풀이가 빨랐다
3-4에서 두 배 이상 차이가 나서 평균 속도는 정렬 쪽이 빨랐다..
이중 for문으로 모든 전화번호의 처음부터 i번째까지의 부분 집합들을 조회해서 오래 걸리는 것 같다...
'''