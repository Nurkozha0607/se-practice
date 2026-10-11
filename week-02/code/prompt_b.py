def analyze_marks(marks, pass_mark=50):
    if not isinstance(marks, list) or not marks:
        raise ValueError("Marks must be a non-empty list")

    for mark in marks:
        if (isinstance(mark, bool)
                or not isinstance(mark, (int, float))
                or not 0 <= mark <= 100):
            raise ValueError("Marks must be numbers between 0 and 100")

    return {
        "average": sum(marks) / len(marks),
        "highest": max(marks),
        "lowest": min(marks),
        "pass_rate": sum(mark >= pass_mark for mark in marks) / len(marks) * 100
    }


print(analyze_marks([80, 65, 40, 90, 55]))