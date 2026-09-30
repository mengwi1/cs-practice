threshold = float(input('Введите порог температуры: '))
n = int(input('Введите количество записей: '))
entries_received = 0
error = 0
exceeding_limit = 0
maxt = 0
average = 0.0
print(f'Введите {n} показаний:')
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
        maxt = max(maxt, x)
        exceeding_limit += 1
    if x <= threshold:
        entries_received += 1
        average += x
