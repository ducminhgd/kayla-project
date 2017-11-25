import collections

if __name__ == '__main__':
    list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]

    # Cannot check if there is any number appear more than twice
    list_len = len(list_of_numbers)
    temp = 0
    for i in range(0, list_len):
        temp = (temp ^ (list_of_numbers[i]) ^ i)
    print('Using XOR: ' + str(temp))

    result = ([item for item, count in collections.Counter(list_of_numbers).items() if count > 1])
    print('Using collections.Counter: ' + str(result))
