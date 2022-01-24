import timeit


text = """what have the romans ever done for us"""


def time_capitals():
    capitals = [char.upper() for char in text]
    return capitals


def time_map_capitals():
    map_capitals = list(map(str.upper, text))
    return map_capitals


def time_words():
    words = [word.upper() for word in text.split(' ')]
    return words


def time_map_words():
    map_words = list(map(str.upper, text.split(' ')))
    return map_words


print(timeit.timeit('time_capitals()', globals=globals(), number=10000))
print(timeit.timeit('time_words()', globals=globals(), number=10000))
print(timeit.timeit('time_map_capitals()', setup='from __main__ import time_map_capitals', number=10000))
print(timeit.timeit(time_map_words, number=10000))
print(time_map_words())
