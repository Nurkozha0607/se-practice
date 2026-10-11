
def analyze_marks(marks, pass_mark=50):
    if not isinstance(marks, list) or not marks:
        raise ValueError("Marks must be a non-empty list")

    def valid_number(value):
        return (
            type(value) in (int, float)
            and 0 <= value <= 100
        )

    if not valid_number(pass_mark):
        raise ValueError("pass_mark must be between 0 and 100")

    for mark in marks:
        if not valid_number(mark):
            raise ValueError("Marks must be numbers from 0 to 100")

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)
    passed = sum(mark >= pass_mark for mark in marks)
    pass_rate = round(passed / len(marks) * 100, 2)

    return {
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "pass_rate": pass_rate
    }


# Tests

# 1. Example
assert analyze_marks([40, 60, 80], 50) == {
    "average": 60.0,
    "highest": 80,
    "lowest": 40,
    "pass_rate": 66.67
}

# 2. Single mark
assert analyze_marks([75]) == {
    "average": 75.0,
    "highest": 75,
    "lowest": 75,
    "pass_rate": 100.0
}

# 3. Decimal marks
assert analyze_marks([40.5, 60.5, 80.5]) == {
    "average": 60.5,
    "highest": 80.5,
    "lowest": 40.5,
    "pass_rate": 66.67
}

# 4. Custom pass_mark
assert analyze_marks([40, 60, 80], 70)["pass_rate"] == 33.33

# 5. Mark exactly equal to pass_mark
assert analyze_marks([50], 50)["pass_rate"] == 100.0

# 6. Invalid inputs
invalid_cases = [
    ([], 50),               # Empty list
    ([40, "hello"], 50),    # Non-numeric value
    ([-5, 60], 50),         # Below 0
    ([50, 105], 50),        # Above 100
    ([True, 60], 50),       # Boolean mark
    ([40, 60], "50"),       # Invalid pass_mark type
    ([40, 60], -1),         # pass_mark below 0
    ([40, 60], 101),        # pass_mark above 100
    ([float("nan")], 50),   # NaN mark
    ([float("inf")], 50)    # Infinite mark
]

for marks, pass_mark in invalid_cases:
    try:
        analyze_marks(marks, pass_mark)
    except ValueError:
        pass
    else:
        raise AssertionError(
            f"Expected ValueError for {marks}, {pass_mark}"
        )

print("All tests passed!")
print(analyze_marks([40, 60, 80], 50))
