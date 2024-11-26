# TODO Написать свою реализацию функции для подсчёта числа вхождение элементов в список
def my_count(l: list, item):
    counter = 0
    for element in l:
        if item in l:
            counter += 1
    return counter
