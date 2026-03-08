def square(number):
    sum = 1
    if number < 1 or number > 64:
        raise ValueError ('square must be between 1 and 64')
    else:
        for i in range(1,number):
            sum = sum * 2
    return sum

def total():
    box_sum = 0
    for i in range(1, 65):
        box = square(i)
        box_sum += box
    return box_sum
