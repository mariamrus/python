for number in range(1, 1001, 2):
    number = number ** 3
    sum_num = 0
    while number > 0:
        digit = number % 10
        sum_num = sum_num + digit
        number = number // 10
        if sum_num % 7 == 0:




