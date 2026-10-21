def count_items(values):
    counts = {}
    for i in values:
        counts[i] = counts.get(i, 0) + 1
    return counts

def unique_sorted(values):
    return sorted(set(values))

