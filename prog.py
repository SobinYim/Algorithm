import re
import subprocess
from os import listdir
from os.path import join, getctime
from urllib.parse import quote
from collections import defaultdict
from typing import Union, Optional


#실행 결과 요약
def cal_res(r: int = 2, eff: bool = False) -> None:
    """
    프로그래머스 실행 결과를 입력받아 평균 실행 시간, 평균 메모리 사용량을 출력합니다.

    :param r: 반올림 자릿수
    :param eff: 효율성 테스트 여부
    """
    text = input().strip("\n")
    text = list(map(lambda x: list(map(lambda y: float(y[:-2]), x.split(", "))), re.findall(r"\((.*?)\)", text)))
    t, memory = zip(*text)
    l = len(t)
    mean_t = round(sum(t) / l, r)
    mean_m = round(sum(memory) / l, r)
    print("[효율성 테스트] " if eff else "", f"평균 실행 시간 : {mean_t} 평균 메모리 사용량: {mean_m}", sep="")

# 마지막으로 수행한 업데이트 조회
def get_latest_problem() -> Optional[bool]:
    """
    README 문서에서 '가장 최근에 해결한 문제'를 찾아 출력합니다.
    파일을 읽어올 수 없다면 False를 반환합니다.
    """
    readme = get_file()
    if not readme:
        print("Error: 파일을 읽어올 수 없음")
        return False
    print("마지막으로 업데이트된 문제는 '%s' 입니다." % re.findall(r"\[(.+)\]", readme)[0])

#조건에 맞는 숫자를 찾아 수정
def change_num(regex: str, content: str, n: int = 1) -> str:
    """
    content에서 주어진 정규식에 해당하는 숫자를 찾아 n 만큼 더하여 반환합니다.

    :param regex: 정규식
    :param content: 대상 문자열
    :param n: 더할 숫자
    :return: 수정된 대상 문자열
    """
    solved_n = int(re.search(regex, content).group()) + n
    return re.sub(regex, str(solved_n), content)

#파일 읽어오기(default=readme)
def get_file(path: str = "./README.md") -> str:
    """
    path의 위치에서 파일을 읽어옵니다.(기본값: README.md)
    파일이 공백 문자와 개행 문자로만 이루어져 있을 경우 빈 문자열을 반환합니다.

    :param path: 파일 위치
    :return: 파일 내용
    """
    try:
        with open(path, "r") as file:
            content = file.read()
        return content if re.sub(r"\s", "", content) else ""
    except:
        return ""

#실제로 해결한 문제 수와 readme 문서 상 해결한 문제 수 매치
def match_file_count(max_lv: int = 3) -> Union[dict,bool]:
    """
    max_lv까지 디렉토리와 README 문서의 일치 여부를 검사합니다.
    일치하지 않는 문제 레벨과 불일치 문제 수를 반환합니다.
    README 파일이 읽히지 않는 경우, False를 반환합니다.

    :param max_lv: 검사할 레벨 수
    :return: 불일치 dict(문제 레벨 : 불일치 수)
    """
    readme = get_file()
    tot_dir, tot_readme = 0, 0 #전체 디렉토리 내 파일의 수, 문서에 명세된 전체 파일의 수
    discrepancy_dict = dict() #불일치 dict(문제 레벨 : 불일치 수)
    if not readme:
        print("Error: 파일을 읽어올 수 없음")
        return False
    print("[Programmers] 해결한 문제")
    for lv in range(1, max_lv + 1):
        dir_count = len(listdir(f"./[Programmers] Lv{lv}"))
        readme_count = int(re.search(rf"(?<=lv{lv}: )\d+(?=\n)", readme).group())
        tot_dir += dir_count
        tot_readme += readme_count
        if dir_count == readme_count:
            print(f"[ 일치 ] Lv{lv}: {dir_count}")
        else:
            discrepancy_dict[lv] = abs(dir_count - readme_count)
            print(f"[불일치] Lv{lv}: {dir_count}(dir) --{readme_count}(readme)--")
    print(f"total: {tot_dir}", f"(dir) --{tot_readme}(readme)--\n" if tot_dir != tot_readme else "", sep="")
    return discrepancy_dict

#readme 일괄 업데이트
def update_readme() -> Optional[bool]:
    """
    디렉토리와 README 문서를 비교하여 새롭게 추가된 부분을 README에 반영합니다.
    README를 읽어오는 데 실패하거나 불일치 dict가 없거나, 파일을 저장하는 데 실패했을 경우 False를 반환합니다.
    """
    discrepancy_dict = match_file_count()
    if not discrepancy_dict:
        print("\n업데이트할 파일이 없습니다.")
        return False
    readme = get_file()
    if not readme:
        print("Error: 파일을 읽어올 수 없음")
        return False
    update_dict = defaultdict(list)  # lv:name
    problem = []  # name, lv, ctime
    for lv, cnt in discrepancy_dict.items():
        files = dict()
        for f in listdir(f"./[Programmers] Lv{lv}"):
            files[f] = getctime(join(f"./[Programmers] Lv{lv}", f))
        new_files = sorted(files.items(), key=lambda x: x[1], reverse=True)[:cnt]
        for f, t in new_files:
            update_dict[lv].append(f)
            if not problem or problem[-1] < t:
                problem = [f, lv, t]
        readme = change_num(rf"(?<=lv{lv}: )\d+(?=\n)", readme, cnt)
    url = f"(https://github.com/SobinYim/Algorithm/blob/main/%5BProgrammers%5D%20Lv{problem[1]}/{quote(problem[0])})"
    readme = change_num(r"(?<=Total\*\*:  )\d+(?=\n)", readme, sum(discrepancy_dict.values()))
    readme = re.sub("\[.+\]", f"[{problem[0].rstrip('.py')}]", readme)
    readme = re.sub(r"\(.+\)", url, readme)
    update_problem = f"Solved problems: programmers"
    for k, v in update_dict.items():
        update_problem += f" lv{k} [[{'], ['.join(f.rstrip('.py') for f in v)}]], "
    update_problem = update_problem.rstrip(", ")
    print(update_problem)
    try:
        with open("./readme.md", "w") as file:
            file.write(readme)
        with open("./update_problem.txt", "w") as file:
            file.write(update_problem)
    except:
        print("Error: 파일을 저장하는 데 실패함")
        return False
    print(f"update complete for {sum(discrepancy_dict.values())} problem solutions!")

#커밋 메세지 생성
def make_commit_message() -> Optional[bool]:
    """
    사전에 사용자가 입력한 메세지와 해결한 문제 목록을 이용하여 커밋 메세지를 생성합니다.
    커밋 메세지를 저장하는 데 실패했을 경우 False를 반환합니다.
    """
    message = get_file("./message.txt")
    update_problems = get_file("./update_problem.txt")
    if not any([message, update_problems]):
        commit_message = ""
    elif message:
        title, *body = message.split("\n")
        commit_message = "\n".join([title + "\n"] + [update_problems] + body)
    else:
        cnt = len(re.findall(r"\[(.*?)\]", update_problems))
        commit_message = f"added {cnt} problem solutions\n\n{update_problems}"
    try:
        with open("./commit_message.txt", "w") as file:
            file.write(commit_message)
    except:
        print("Error: 파일을 저장하는 데 실패함")
        return False

#레포지토리 업데이트
def run_bat() -> None:
    """
    배치 파일을 실행하여 레포지토리를 업데이트합니다.
    커밋 메세지가 없다면 사용자가 커밋 메세지를 입력하는 update_repository_lite를 실행합니다.
    """
    commit_message = get_file("./commit_message.txt")
    if commit_message:
        subprocess.run([".\\update_repository.bat"])
    else:
        subprocess.run([".\\update_repository_lite.bat"])


if __name__ == "__main__":
    update_readme()
    make_commit_message()
    run_bat()
    input()
