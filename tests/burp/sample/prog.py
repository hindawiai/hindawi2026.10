# count up to the limit
def count_up(limit):
    total = 0
    for index in range(limit):
        total = total + index
    return total
print(count_up(10))
