import datetime

# 파일 경로
file_path = "study_log.txt"

# 메뉴 출력 함수
def print_menu():
    print("1. 공부 기록하기")
    print("2. 공부 기록 조회하기")
    print("3. 종료하기")

# 공부 기록 함수
def log_study_time():
    study_time = int(input("공부한 시간을 분 단위로 입력하세요: "))
    now = datetime.datetime.now()
    study_date = now.strftime("%Y-%m-%d")
    study_time_str = str(study_time)
    log_line = f"{study_date}\t{study_time_str}\n"
    with open(file_path, "a") as f:
        f.write(log_line)
    print("공부 기록이 저장되었습니다.")

# 공부 기록 조회 함수
def show_study_log():
    with open(file_path, "r") as f:
        log_lines = f.readlines()
    total_study_time = 0
    for line in log_lines:
        date_str, time_str = line.strip().split("\t")
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        time = int(time_str)
        print(f"{date.strftime('%Y년 %m월 %d일')}: {time}분")
        total_study_time += time
    print(f"총 공부 시간: {total_study_time}분")

# 프로그램 시작
print("공부 매니징 프로그램을 시작합니다.")

while True:
    print_menu()
    choice = input("원하는 작업의 번호를 입력하세요: ")
    if choice == "1":
        log_study_time()
    elif choice == "2":
        show_study_log()
    elif choice == "3":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")
