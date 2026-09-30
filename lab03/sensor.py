threshold = float(input('Введите порог температуры: '))
n = int(input('Введите количество записей: '))
entries_received = 0
error = 0
exceeding_limit = 0
maxt = 0
average = 0.0
for i in range(n):
    x = input()
    if x == 'error':
        error += 1
        entries_received +=1
        continue
    x = float(x)
    if x > threshold:
        entries_received += 1
        average += x
        exceeding_limit += 1
    if x <= threshold:
        entries_received += 1
        average += x
    if abs(x) > abs(maxt):
        maxt = x
print(f'{entries_received}')
print(f'{error}')
print(f'{exceeding_limit}')
print(f'{maxt:.1f}')
print(f'{average/(entries_received - error):.1f}')