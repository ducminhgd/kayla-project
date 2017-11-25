import collections

if __name__ == "__main__":
    list_of_string = [
        "Hello",
        "I'm",
        "Minh",
        "Hello",
    ]

    print([item for item, count in collections.Counter(list_of_string).items() if count > 1])
