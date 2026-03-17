# unittest

def reverse_string(s):
    return s[::-1]

def count_letters(s):
    return sum(1 for c in s if c.isalpha())


def remove_duplicates(lst):
    return list(set(lst))


# pytest
def get_even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

def find_max(lst):
    if not lst:
        raise ValueError("Empty list")
    return max(lst)