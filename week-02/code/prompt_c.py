
def analyze_marks(marks, pass_mark=50):
    if not isinstance(marks, list) or not marks:
        raise ValueError("Marks must be a non-empty list")

    if (isinstance(pass_mark, bool)
            or not isinstance(pass_mark, (int, float))
            or not 0 <= pass_mark <= 100):
        raise ValueError("Invalid pass mark")

    for mark in marks:
        if (isinstance(mark, bool)
                or not isinstance(mark, (int, float))
                or not 0 <= mark <= 100):
            raise ValueError("Invalid mark")

    return {
        "average": sum(marks) / len(marks),
        "highest": max(marks),
        "lowest": min(marks),
        "pass_rate": round(
            sum(m >= pass_mark for m in marks) / len(marks) * 100, 2
        )
    }


# Tests
assert analyze_marks([40, 60, 80], 50) == {
    "average": 60,
    "highest": 80,
    "lowest": 40,
    "pass_rate": 66.67
}

assert analyze_marks([75])["pass_rate"] == 100.0
assert analyze_marks([40.5, 60.5])["average"] == 50.5
assert analyze_marks([40, 60, 80], 70)["pass_rate"] == 33.33

# Invalid input tests
for invalid in [[], [40, "text"], [-5, 60], [50, 105]]:
    try:
        analyze_marks(invalid)
        raise AssertionError("Expected ValueError")
    except ValueError:
        pass

print("All tests passed!")
