__author__: str = "730567389"


def invert(begin: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary"""
    end: dict[str, str] = {}
    for key in begin:
        keyflip: str = begin[key]
        if keyflip in end:
            raise KeyError("Cannot have Duplicate Keys")
        end[keyflip] = key
    return end


def count(values: list[str]) -> dict[str, int]:
    """Counts the amount of values in a list"""
    result: dict[str, int] = {}
    idx: int = 0
    while idx < len(values):
        if values[idx] in result:
            result[values[idx]] += 1
        else:
            result[values[idx]] = 1
        idx += 1
    return result


def favorite_color(favcolor: dict[str, str]) -> str:
    """Determines the most common favorite color from a dictionary of values"""
    count_input: list[str] = []
    for key in favcolor:
        count_input.append(favcolor[key])
    count_output: dict[str, int] = count(count_input)

    highest_count: int = 0
    fav_color: str = ""
    for name in count_output:
        if count_output[name] > highest_count + 1:
            fav_color: str = name
            highest_count += 1
    return fav_color


def bin_len(strings: list[str]) -> dict[int, set[str]]:
    """Organizes a list of strings into a dictionary where the key is the length of the string input and the value is a set of items from the list that are the length of the integer"""
    end: dict = {}
    for elem in strings:
        length = len(elem)
        if length in end:
            end[length].add(elem)
        else:
            end[length] = {elem}
    return end
