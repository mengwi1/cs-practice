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

