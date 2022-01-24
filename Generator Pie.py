def odd_numbers():
    n = 0
    while True:
        if n % 2 != 0:
            yield n
        n += 1


def pie_value():
    summation = 0
    odd = odd_numbers()
    while True:
        summation = summation + (4 / next(odd))
        yield summation
        summation = summation - (4 / next(odd))
        yield summation


pie = pie_value()
for i in range(100):
    print(next(pie))

