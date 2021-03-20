time_in_sec = int(input('Введите время в сек'))
if 60 <= time_in_sec <= 3600:
    time_in_min = time_in_sec // 60
    remains_sec = time_in_sec % 60
    print(f"{time_in_min} мин {remains_sec} сек")
elif 86400 > time_in_sec >= 3600:
    time_in_hour = time_in_sec // 3600
    remain_sec = time_in_sec % 3600
    time_in_min = remain_sec // 60
    sek = remain_sec % 60
    print(f"{time_in_hour} час {time_in_min} мин {sek} сек")
elif time_in_sec >= 86400:
    count_day = time_in_sec // 86400
    time_in_hour = time_in_sec % 86400
    remain_hour = time_in_hour // 3600
    time_in_min = time_in_hour % 3600
    remain_min = time_in_min // 60
    time_in_sec = time_in_min % 60
    print(f"{count_day} дн {remain_hour} час {remain_min} мин {time_in_sec} сек")
