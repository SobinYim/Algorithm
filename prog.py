import re
from urllib.parse import quote

#실행 결과 요약
def cal_res(r=2):
    text=input().strip("\n")
    text=list(map(lambda x: list(map(lambda y: float(y[:-2]), x.split(", "))), re.findall(r"\((.*?)\)", text)))
    t, memory = zip(*text)
    l=len(t)
    mean_t=round(sum(t)/l,r)
    mean_m=round(sum(memory)/l,r)
    print(f"평균 실행 시간 : {mean_t} 평균 메모리 사용량: {mean_m}")

#조건에 맞는 숫자를 찾아 수정
def change_num(regex,content):
    solved_n=int(re.search(regex,content).group())+1
    return re.sub(regex,str(solved_n),content)

#README 파일 업데이트
def update_readme(lv,problem_name):
    url=f"(https://github.com/SobinYim/Algorithm/blob/main/%5BProgrammers%5D%20Lv{lv}/{quote(problem_name)}.py)"
    try:
        with open("./readme.md","r") as file:
            content=file.read()
    except:
        print("Error: 파일을 읽어올 수 없음")
        return False
    edited_content=change_num(rf"(?<=lv{lv}: )\d+(?=\n)",content)
    edited_content=change_num(r"(?<=Total\*\*:  )\d+(?=\n)",edited_content)
    edited_content=re.sub(r"\[.+\]",f"[{problem_name}]",edited_content)
    edited_content=re.sub(r"\(.+\)",url,edited_content)
    try:
        with open("./readme.md","w") as file:
            file.write(edited_content)
    except:
        print("Error: 파일을 저장하는 데 실패함")
        return False
    print(f"lv{lv}. [{problem_name}] update complete!")