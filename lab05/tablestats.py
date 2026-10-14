def read_rows(lines: list[str]) -> list[dict]:
    rows = []
    header = None
    for line in lines:
        line = line.strip()
        if not line:
            continue
        fields = [field.strip() for field in line.split(",")]
        if header is None:
            header = fields
            continue
        if len(fields) != len(header):
            continue
        row = dict(zip(header, fields))
        rows.append(row)
    return rows

def count_types(rows: list[dict]) -> dict:
    counts = {}
    for row in rows:
        kind = row["тип"]
        counts[kind] = counts.get(kind, 0) + 1
    return counts

def total_minutes(rows: list[dict], kind : str) -> float:
    total = 0.0
    for row in rows:
        if row["тип"] != kind:
            continue
        try:
            minutes = float(row["минуты"].replace(",", "."))
        except ValueError:
            continue
        total += minutes
    return round(total, 1)

def to_csv(counts: dict) -> str:
    lines = ["тип, количество"]
    for kind in sorted(counts):
        lines.append(f"{kind}, {counts[kind]}")
    return "\n".join(lines) + "\n"

