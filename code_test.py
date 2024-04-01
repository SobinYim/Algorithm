import re
def match(text):
    pattern = r'\((.*?)\)'  # 괄호 안에 있는 모든 문자를 찾는다
    matches = re.findall(pattern, text)[0]
    return matches

def cal_res(r=2):
    text=input()
    text=text.split("\n")
    text=list(map(lambda x: list(map(lambda x: float(x[:-2]),match(x).split(", "))),text))
    t, memory = zip(*text)
    l=len(t)
    mean_t=round(sum(t)/l,r)
    mean_m=round(sum(memory)/l,r)
    print(f"평균 실행 시간 : {mean_t} 평균 메모리 사용량: {mean_m}")
