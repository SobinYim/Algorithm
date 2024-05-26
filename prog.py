import re
import subprocess
from os import listdir
from os.path import join,getctime
from urllib.parse import quote
from collections import defaultdict

#실행 결과 요약
def cal_res(r=2,eff=False):
    text=input().strip("\n")
    text=list(map(lambda x: list(map(lambda y: float(y[:-2]), x.split(", "))), re.findall(r"\((.*?)\)", text)))
    t, memory = zip(*text)
    l=len(t)
    mean_t=round(sum(t)/l,r)
    mean_m=round(sum(memory)/l,r)
    print("[효율성 테스트]" if eff else "",f"평균 실행 시간 : {mean_t} 평균 메모리 사용량: {mean_m}",sep="")

#조건에 맞는 숫자를 찾아 수정
def change_num(regex,content,n=1):
    solved_n=int(re.search(regex,content).group())+n
    return re.sub(regex,str(solved_n),content)

#readme 파일 읽어오기
def get_readme():
    try:
        with open("./readme.md","r") as file:
            content=file.read()
        return content
    except:
        return False

#README 파일 업데이트
def update_readme(lv,problem_name):
    confirm=input(f"업데이트하려는 문제가 lv{lv}, {problem_name} 문제가 맞나요?(y/n)")
    if confirm.lower()!="y":
        print("업데이트 취소됨")
        return False
    url=f"(https://github.com/SobinYim/Algorithm/blob/main/%5BProgrammers%5D%20Lv{lv}/{quote(problem_name)}.py)"
    content=get_readme()
    if not content:
        print("Error: 파일을 읽어올 수 없음")
        return False
    prev_problem=re.findall(r"\[(.+)\]",content)[0]
    if prev_problem==problem_name:
        print("이미 업데이트한 문제")
        return False
    edited_content=change_num(rf"(?<=lv{lv}: )\d+(?=\n)",content)
    edited_content=change_num(r"(?<=Total\*\*:  )\d+(?=\n)",edited_content)
    edited_content=edited_content.replace(prev_problem,problem_name)
    edited_content=re.sub(r"\(.+\)",url,edited_content)
    try:
        with open("./readme.md","w") as file:
            file.write(edited_content)
    except:
        print("Error: 파일을 저장하는 데 실패함")
        return False
    print(f"lv{lv}. [{problem_name}] update complete!")

#마지막으로 수행한 업데이트 조회
def get_latest_problem():
    content=get_readme()
    if not content:
        print("Error: 파일을 읽어올 수 없음")
        return False
    print("마지막으로 업데이트된 문제는 '%s' 입니다." % re.findall(r"\[(.+)\]", content)[0])

#실제로 해결한 문제 수와 readme 문서 상 해결한 문제 수 매치
def match_file_count(max_lv=3):
    content=get_readme()
    tot_dir,tot_readme=0,0
    discrepancy_dict=dict()
    if not content:
        print("Error: 파일을 읽어올 수 없음")
        return False
    print("[Programmers] 해결한 문제")
    for lv in range(1,max_lv+1):
        dir_count=len(listdir(f"./[Programmers] Lv{lv}"))
        readme_count=int(re.search(rf"(?<=lv{lv}: )\d+(?=\n)",content).group())
        tot_dir+=dir_count
        tot_readme+=readme_count
        if dir_count==readme_count:
            print(f"[ 일치 ] Lv{lv}: {dir_count}")
        else:
            discrepancy_dict[lv]=abs(dir_count-readme_count)
            print(f"[불일치] Lv{lv}: {dir_count}(dir) --{readme_count}(readme)--")
    print(f"total: {tot_dir}",f"(dir) --{tot_readme}(readme)--\n" if tot_dir!=tot_readme else "",sep="")
    return discrepancy_dict

#readme 일괄 업데이트
def auto_update_readme():
    discrepancy_dict=match_file_count()
    if not discrepancy_dict:
        print("\n업데이트할 파일이 없습니다.")
        return False
    content=get_readme()
    if not content:
        print("Error: 파일을 읽어올 수 없음")
        return False
    update_dict=defaultdict(list) #lv:name
    problem=[] #name, lv, ctime
    for lv,cnt in discrepancy_dict.items():
        files = dict()
        for f in listdir(f"./[Programmers] Lv{lv}"):
            files[f]=getctime(join(f"./[Programmers] Lv{lv}",f))
        new_files=sorted(files.items(),key=lambda x:x[1],reverse=True)[:cnt]
        for f,t in new_files:
            update_dict[lv].append(f)
            if not problem or problem[-1]<t:
                problem=[f,lv,t]
        content=change_num(rf"(?<=lv{lv}: )\d+(?=\n)", content,cnt)
    url=f"(https://github.com/SobinYim/Algorithm/blob/main/%5BProgrammers%5D%20Lv{problem[1]}/{quote(problem[0])})"
    content=change_num(r"(?<=Total\*\*:  )\d+(?=\n)",content,sum(discrepancy_dict.values()))
    content=re.sub("\[.+\]",f"[{problem[0].rstrip('.py')}]",content)
    content=re.sub(r"\(.+\)",url,content)
    update_problem=f"Solved problems: programmers"
    for k,v in update_dict.items():
        update_problem+=f" lv{k} [[{'], ['.join(f.rstrip('.py') for f in v)}]], "
    update_problem=update_problem.rstrip(", ")
    print(update_problem)
    try:
        with open("./readme.md","w") as file:
            file.write(content)
        with open("./update_problem.txt","w") as file:
            file.write(update_problem)
    except:
        print("Error: 파일을 저장하는 데 실패함")
        return False
    print(f"update complete for {sum(discrepancy_dict.values())} problem solutions!")

#커밋 메세지 만들기
def make_commit_message():
    try:
        with open("./message.txt","r") as file:
            message = file.read()
        with open("./update_problem.txt","r") as file:
            update_problems = file.read()
    except:
        print("Error: 파일을 읽어올 수 없음")
        return False
    title,*body=message.split("\n")
    commit_message="\\n".join([title+"\\n"]+[update_problems]+body)
    try:
        with open("./commit_message.txt","w") as file:
            file.write(commit_message)
    except:
        print("Error: 파일을 저장하는 데 실패함")
        return False


if __name__=="__main__":
    auto_update_readme()
    make_commit_message()
    subprocess.run([".\\update_repository.bat"])
    input()