from collections import deque

food_portions = [int(n) for n in input().split(', ')]
stamina = deque(int(n) for n in input().split(', '))

mountain_peaks = deque([
            ("Vihren", 80),
            ("Kutelo", 90),
            ("Banski Suhodol", 100),
            ("Polezhan", 60),
            ("Kamenitza", 70)
])

day = 1
conquered_peaks = []
total_stats_list = deque()

while True:
    if len(conquered_peaks) == 5:
        print('Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK')
        print(f'Conquered peaks:', *conquered_peaks, sep='\n')
        break

    if day > 7 or not food_portions or not stamina:
        print('Alex failed! He has to organize his journey better next time -> @PIRINWINS')
        break

    food = food_portions.pop()
    current_stamina = stamina.popleft()

    total_stats = food + current_stamina
    total_stats_list.append(total_stats)

    next_peak = mountain_peaks.popleft()

    if total_stats >= next_peak[1]:
        conquered_peaks.append(next_peak[0])
        day += 1

    else:
        mountain_peaks.appendleft(next_peak)
        day += 1
