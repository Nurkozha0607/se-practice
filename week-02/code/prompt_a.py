def analyze_marks(marks, pass_mark=50):
    if not marks:
        raise ValueError("Marks cannot be empty")

    for mark in marks:
        if not isinstance(mark, (int, float)) or not 0 <= mark <= 100:
            raise ValueError("Invalid mark")

    return {
        "average": sum(marks) / len(marks),
        "highest": max(marks),
        "lowest": min(marks),
        "pass_rate": sum(m >= pass_mark for m in marks) / len(marks) * 100
    }


marks = [85, 70, 45, 90, 60]
print(analyze_marks(marks))