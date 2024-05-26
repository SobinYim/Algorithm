#sol
def solution(bridge_length, weight, truck_weights): #다리에 올라갈 수 있는 트럭 수, 다리가 견딜 수 있는 무게, 트럭 별 무게
    bridge = "".zfill(bridge_length) #다리
    elem = [] #다리 위에 있는 차량
    ans, tot = bridge_length, 0 #시간, 다리 위 차량의 무게 합
    for truck in truck_weights:
        while tot + truck > weight: #트럭이 올라왔을 때 하중이 제한 무게를 초과하는 동안 루프
            ans += (idx := bridge.index("t") + 1) #가장 선두의 트럭 위치==트럭이 통과하기까지 걸리는 시간
            tot -= elem.pop(0) #트럭을 통과
            if tot + truck > weight: #여전히 제한 무게를 초과하면
                bridge = bridge[idx:].ljust(bridge_length, "0")
            else:
                tot += truck
                bridge = bridge[idx:].ljust(bridge_length - 1, "0") + "t"
                elem.append(truck)
                break
        else:
            ans += 1
            tot += truck if bridge[0]=="0" else truck - elem.pop(0)
            bridge = bridge[1:] + "t"
            elem.append(truck)
    return ans

#sol1
from collections import deque
def solution(bridge_length, weight, truck_weights): #다리에 올라갈 수 있는 트럭 수, 다리가 견딜 수 있는 무게, 트럭 별 무게
    truck_weights.reverse()
    bridge = "".zfill(bridge_length) #다리
    elem = deque() #다리 위에 있는 차량
    ans, tot = bridge_length, 0 #시간, 다리 위 차량의 무게 합
    while truck_weights: #대기중인 트럭이 존재하면 루프
        if tot + truck_weights[-1] > weight: #트럭이 올라왔을 때 하중이 제한 무게를 초과하면
            ans += (idx := bridge.index("t") + 1)
            tot -= elem.popleft() #트럭을 통과
            if tot + truck_weights[-1] > weight: #여전히 제한 무게를 초과하면
                bridge = bridge[idx:].ljust(bridge_length, "0")
                continue
            else:
                bridge = bridge[idx:].ljust(bridge_length - 1, "0") + "t"
        else:
            ans += 1
            if bridge[0].isalpha(): #다리를 빠져나오는 트럭이 있다면
                tot -= elem.popleft()
            bridge = bridge[1:] + "t"
        truck = truck_weights.pop()
        tot += truck
        elem.append(truck)
    return ans

#sol2
from collections import deque
def solution(bridge_length, weight, truck_weights): #다리에 올라갈 수 있는 트럭 수, 다리가 견딜 수 있는 무게, 트럭 별 무게
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length) #다리
    ans, tot = 0, 0 #시간, 다리 위 차량의 무게 합
    while truck_weights: #대기중인 트럭이 존재하면 루프
        ans += 1
        if tot + truck_weights[0] > weight: #트럭이 올라왔을 때 하중이 제한 무게를 초과하면
            if not bridge[0]: #비어있다면 회전
                bridge.rotate(-1)
            else:
                tot -= bridge.popleft() #트럭을 통과
                if tot + truck_weights[0] > weight: #여전히 제한 무게를 초과하면
                    bridge.append(0)
                else:
                    truck = truck_weights.popleft()
                    tot += truck
                    bridge.append(truck)
        else:
            truck = truck_weights.popleft()
            tot += truck - bridge.popleft()
            bridge.append(truck)
    return ans + bridge_length

'''
sol
평균 실행 시간 : 0.12 평균 메모리 사용량: 10.2
sol1
평균 실행 시간 : 0.13 평균 메모리 사용량: 10.13
sol2
평균 실행 시간 : 6.21 평균 메모리 사용량: 10.26

sol2>sol1>sol 순으로 짰다

sol은 while 대신 for문을 사용했고, elem에 list를 사용했고, 가독성에 조금 더 신경 썼다
sol1에서 공통된 부분을 빼서 한 번에 처리함으로써 불필요한 중복을 막았는데 조금 혼란한 것 같아서 그 부분을 수정했다
sol의 루프를 탈출할 때 break를 쓰기 때문에 else문은 무게 제한을 초과하지 않는 경우에만 실행된다

디테일은 다르지만 sol과 sol1은 접근법이 같다
bridge를 문자열로 만들어서 빈 공간에는 0을 채우고 트럭이 있는 공간에는 t를 넣었다
처음에는 index를 lstrip("0")으로 길이를 재서 찾을까 했는데
생각해 보니 트럭 무게를 굳이 넣을 필요가 없으니 일괄적으로 t로 넣고 t의 위치를 찾기로 했다

sol2는 while문을 사용했고, 매 초마다 다리 위 상황을 갱신하는 방식이라 아무래도 비효율적이다....
sol2랑 같은 로직의 풀이가 있었는데,,, 
처음에 bridge를 pop하고 하중 계산해서 0 혹은 트럭의 무게를 append해줬다,,, 심플한 방법이 있는데 괜히 돌아간 셈이다....


다른 사람의 풀이:
def solution(bridge_length, weight, truck_weights):
    on_the_bridge = []
    i = 0
    time = 0
    for truck in truck_weights:
        if weight >= truck:
            time += 1
        else:
            while weight < truck:
                completed = on_the_bridge[i]
                i += 1
                weight += completed[0]
                time = completed[1] + bridge_length
        on_the_bridge.append([truck, time])

        while on_the_bridge[i][1] + bridge_length <= time:
            weight += on_the_bridge[i][0]
            i += 1
        weight -= truck
    return on_the_bridge.pop()[1] + bridge_length
평균 실행 시간 : 0.08 평균 메모리 사용량: 10.23
다리 위의 트럭 무게의 합을 구하지 않고 weight에 더하고 빼줌으로써 다리 위로 더 올라갈 수 있는 무게로 만들었다!
다리 위에 트럭이 몇 대 있느냐가 아니라 하중이 제한 무게를 초과하면 트럭을 보낸다는 것에 초점을 맞췄다
다리 위 선두 트럭의 인덱스를 저장하여 선두 트럭이 들어간 시간이랑 현재 시간을 이용하여 트럭이 나와야 할 시간을 계산하고
하중이 초과하거나 트럭이 다리에서 빠져나올 시간이 되면 이를 이용해 트럭을 보낸다
발상 좋다!
'''