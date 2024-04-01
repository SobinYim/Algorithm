def solution(dirs): #입력 방향키
    x,y=0,0 #x,y 위치
    x_axis,y_axis=[],[] #방문
    for i in dirs:
        if i=="D" and y>-5: #아래로 이동, y좌표가 -5 초과일 때
            y_axis.append((x,y))
            y-=1
        elif i=="U" and y<5: #위로 이동, y좌표가 5 미만일 때
            y+=1
            y_axis.append((x,y))
        elif i=="L" and x>-5: #왼쪽으로 이동, x좌표가 -5 초과일 때
            x_axis.append((x,y))
            x-=1
        elif i=="R" and x<5: #오른쪽으로 이동, x좌표가 5 미만일 때
            x+=1
            x_axis.append((x,y))
    return len(set(x_axis))+len(set(y_axis)) #중복 제거하여 길이의 합 반환

'''
평균 실행 시간 : 0.055 평균 메모리 사용량: 10.212

방문했던 길은 x축과 y축으로 나누어서 저장했다
위치를 업데이트하는 시점을 달리해 방향에 관계없이 정확하게 방문했던 길을 저장했다..
set를 처음에 만들지 않고 list를 나중에 set로 만든 이유는... 그게 빨라서다!
왜인지는 모르겠는데 set는 add로 추가하는 것보다 list로 만든 후 나중에 set 변환하는 게 빠른 경우가 많았다
'''