from collections import Counter
from typing import Generator

def load_logs(file_path: str) -> Generator:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError as fnfe:
        print(fnfe.strerror)
        raise FileNotFoundError
            
def parse_log_line(line: str) -> dict:
    try:
        date, time, status, *message = line.split(" ")
        log_obj = {
            "date": date,
            "time": time,
            "status": status,
            "message": " ".join(message)
        }
        return log_obj
    except ValueError:
        print("Log file is empty")
        raise ValueError

def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_logs = list(filter(lambda status: status.get("status").lower() == level.lower(), logs))
    return filtered_logs

def count_logs_by_level(logs: list) -> dict:
    counted = Counter(item["status"] for item in logs)
    return dict(counted)

def display_log_counts(counts: dict):
    top_bottom = "\n*************************************************\n"
    print(top_bottom, ", ".join([" = ".join(str(i) for i in item) for item in counts.items()]), top_bottom)
    return

def display_filtered_log(logs: list, status):
    if logs:
        welcome_msg = f"Logs details for status {status.upper()}:"
        print(welcome_msg)
        for item in logs:
            date, time, _, message = item.values()
            print(date, time, "-", message)
    else:
        print(f"No logs found with {status.upper()} status")