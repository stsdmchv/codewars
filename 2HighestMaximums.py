''' Search two highest maximums. '''


def two_maximums(numbers):
    arrayOfNumbers = [ int(item) for item in numbers ]
    firstMaximum = secondMaximum = min(arrayOfNumbers)
    for item in arrayOfNumbers:
        if item >= firstMaximum:
            secondMaximum = firstMaximum
            firstMaximum = item
        elif item > secondMaximum:
            secondMaximum = item
    return [secondMaximum, firstMaximum]

def two_max(numbers):
    return sorted(numbers)[-2:]

two_maximums = lambda numbers:sorted(numbers)[-2:]
