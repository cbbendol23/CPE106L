#stats.py

def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    sorted_number = sorted(numbers)
    size = len(numbers)

    mid = size // 2

    if size % 2 == 0:
        almost_mid = (sorted_number[mid] + sorted_number[mid - 1])
        return almost_mid / 2
    else:
        return sorted_number[mid]

def mode(numbers):
    return max(set(numbers), key=numbers.count)