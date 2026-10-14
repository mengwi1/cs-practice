from pathlib import Path
from tablestats import *

def main():
    folder = Path(__file__).resolve().parent
    filename = input().strip()
    path = folder / filename
    with open(path, encoding = 'utf-8') as table:
        rows = read_rows(table)

    counts = count_types(rows)

    print(len(rows))
    print(len(counts))
    print(total_minutes(rows, "ошибка"))
    summary_path = folder / "summary.csv"
    with open(summary_path, "w",  encoding = 'utf-8') as out:
        out.write(to_csv(counts))
