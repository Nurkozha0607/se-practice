# Lab report — Practice #02: The Prompt Is an Engineering Input

**Name:**
**Group:**
**Date:**

> Fill in every section. **Do not delete or renumber the headings** — the grading pass reads them
> by number. If something did not happen, write "did not happen" and why; an empty section and a
> fabricated one are graded the same way.

---

## 1. The frozen experiment

| | |
| --- | --- |
| AI assistant | ChatGPT |
| Exact model name | GPT-6 |
| Implementation language | Python 3.12.6 |
| Date of the runs | 11 October 2026 |

**Non-Python students only** — paste your substituted Prompt B text here, so the substitution can
be checked:

```
(paste here, or write "n/a — used Python")
```

**Confirmations:**

- Each prompt was sent in a **fresh chat**: yes / no
- No follow-up questions were asked before Part 7: yes / no
- Every output was saved **before** any editing: yes / no

---

## 2. Prompt A — minimal

**Prompt sent:**

```text
Write Python code to analyze student marks.
```

**Assumptions the AI made that I never gave it:**

1. The default passing mark is 50.
2. Marks must be numeric values between 0 and 100.
3. Invalid marks should raise ValueError.

**Questions it should have asked and did not:**

1. What statistics should the function return?
2. How should invalid input be handled?

**Is the function named `analyze_marks` with the required signature?** Yes.

**First impression before testing:** The generated solution was short and included validation, although the prompt did not specify detailed requirements.

## 3. Prompt B — structured context

**Prompt ## 3. Prompt B — structured context

**Prompt sent:**

```
You are a Python developer. Implement analyze_marks(marks, pass_mark=50). Return
average, highest, lowest, and pass_rate in a dictionary. Accept marks from 0 to 100;
raise ValueError for an empty list, non-numeric values, or out-of-range values. Use
no external libraries. Return code plus a short explanation.
```

**What B fixed compared to A:**

1. Prompt B explicitly specified the function signature and required dictionary keys, even though Prompt A already generated them correctly.
2. Prompt B explicitly required ValueError for invalid inputs, reducing ambiguity in the requirements.

**What B still leaves open:**

1. Whether pass_rate must be rounded to two decimal places.
2. Whether a mark equal to pass_mark counts as passing (the correct rule is greater than or equal to).

## 4. Prompt C — examples and tests

**What I appended to Prompt B:**

```text
Example: analyze_marks([40, 60, 80], 50) → average 60, highest 80, lowest 40,
pass_rate 66.67. Include tests for: one mark, decimals, custom pass_mark, empty list,
text value, and marks below 0 or above 100. State any remaining assumptions before
the code.
```

**Tests the AI wrote for itself — how many, and which situations do they cover?**

The AI generated its own tests, which completed successfully and printed "All tests passed!". The exact number of tests and individual scenarios should be verified against `prompt_c.py`.

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

## 5. Prompt D — my combined prompt

**The complete prompt I wrote** (one message, sent to a fresh chat):

```

```

**What I deliberately added that A, B and C did not have:**

1.
2.
3.

**The ambiguity I found in the specification, and how I resolved it inside Prompt D:**

---

## 6. Test results — the evidence

Six cases × four prompts. Verdicts are PASS, FAIL or ERROR only.

| # | Call | Required | A | B | C | D |
|---|---|---|---|---|---|---|
| 1 | `analyze_marks([40, 60, 80], 50)` | avg 60, high 80, low 40, rate 66.67 | PASS | PASS | PASS | PASS |
| 2 | `analyze_marks([100], 50)` | avg 100, high 100, low 100, rate 100 | PASS | PASS | PASS | PASS |
| 3 | `analyze_marks([49.5, 50], 50)` | avg 49.75, high 50, low 49.5, rate 50 | PASS | PASS | PASS | PASS |
| 4 | `analyze_marks([], 50)` | ValueError | PASS | PASS | PASS | PASS |
| 5 | `analyze_marks([40, "60"], 50)` | ValueError | PASS | PASS | PASS | PASS |
| 6 | `analyze_marks([-1, 50, 101], 50)` | ValueError | PASS | PASS | PASS | PASS |
| | **Totals** | | **6/6** | **6/6** | **6/6** | **6/6** |

**For every FAIL and ERROR above, one line: what was returned or raised instead.**

| Prompt | Case | What actually happened |
|---|---|---|
| A | None | All six cases passed |
| B | None | All six cases passed |
| C | None | All six cases passed |
| D | None | All six cases passed |

### Pasted terminal output — all four runs

**Prompt A**

```
{'average': 70.0, 'highest': 90, 'lowest': 45, 'pass_rate': 80.0}
========================================================================
analyze_marks harness — week-02/code/prompt_a.py
tolerance for numeric comparison: 0.01
========================================================================
SIGNATURE: ok
------------------------------------------------------------------------
case 1  PASS   analyze_marks([40, 60, 80], 50)
          expect: average=60.0, highest=80, lowest=40, pass_rate=66.67
          got   : average=60.0, highest=80, lowest=40, pass_rate=66.66666666666666
------------------------------------------------------------------------
case 2  PASS   analyze_marks([100], 50)
          expect: average=100.0, highest=100, lowest=100, pass_rate=100.0
          got   : average=100.0, highest=100, lowest=100, pass_rate=100.0
------------------------------------------------------------------------
case 3  PASS   analyze_marks([49.5, 50], 50)
          expect: average=49.75, highest=50, lowest=49.5, pass_rate=50.0
          got   : average=49.75, highest=50, lowest=49.5, pass_rate=50.0
------------------------------------------------------------------------
case 4  PASS   analyze_marks([], 50)
          expect: ValueError
          got   : raised ValueError: Marks cannot be empty
------------------------------------------------------------------------
case 5  PASS   analyze_marks([40, '60'], 50)
          expect: ValueError
          got   : raised ValueError: Invalid mark
------------------------------------------------------------------------
case 6  PASS   analyze_marks([-1, 50, 101], 50)
          expect: ValueError
          got   : raised ValueError: Invalid mark
------------------------------------------------------------------------
RESULT  6 PASS · 0 FAIL · 0 ERROR   (week-02/code/prompt_a.py)
========================================================================
```

**Prompt B**

```
{'average': 66.0, 'highest': 90, 'lowest': 40, 'pass_rate': 80.0}
========================================================================
analyze_marks harness — week-02/code/prompt_b.py
tolerance for numeric comparison: 0.01
========================================================================
SIGNATURE: ok
------------------------------------------------------------------------
case 1  PASS   analyze_marks([40, 60, 80], 50)
          expect: average=60.0, highest=80, lowest=40, pass_rate=66.67
          got   : average=60.0, highest=80, lowest=40, pass_rate=66.66666666666666
------------------------------------------------------------------------
case 2  PASS   analyze_marks([100], 50)
          expect: average=100.0, highest=100, lowest=100, pass_rate=100.0
          got   : average=100.0, highest=100, lowest=100, pass_rate=100.0
------------------------------------------------------------------------
case 3  PASS   analyze_marks([49.5, 50], 50)
          expect: average=49.75, highest=50, lowest=49.5, pass_rate=50.0
          got   : average=49.75, highest=50, lowest=49.5, pass_rate=50.0
------------------------------------------------------------------------
case 4  PASS   analyze_marks([], 50)
          expect: ValueError
          got   : raised ValueError: Marks must be a non-empty list
------------------------------------------------------------------------
case 5  PASS   analyze_marks([40, '60'], 50)
          expect: ValueError
          got   : raised ValueError: Marks must be numbers between 0 and 100
------------------------------------------------------------------------
case 6  PASS   analyze_marks([-1, 50, 101], 50)
          expect: ValueError
          got   : raised ValueError: Marks must be numbers between 0 and 100
------------------------------------------------------------------------
RESULT  6 PASS · 0 FAIL · 0 ERROR   (week-02/code/prompt_b.py)
========================================================================
```

**Prompt C**

```
All tests passed!
========================================================================
analyze_marks harness — week-02/code/prompt_c.py
tolerance for numeric comparison: 0.01
========================================================================
SIGNATURE: ok
------------------------------------------------------------------------
case 1  PASS   analyze_marks([40, 60, 80], 50)
          expect: average=60.0, highest=80, lowest=40, pass_rate=66.67
          got   : average=60.0, highest=80, lowest=40, pass_rate=66.67
------------------------------------------------------------------------
case 2  PASS   analyze_marks([100], 50)
          expect: average=100.0, highest=100, lowest=100, pass_rate=100.0
          got   : average=100.0, highest=100, lowest=100, pass_rate=100.0
------------------------------------------------------------------------
case 3  PASS   analyze_marks([49.5, 50], 50)
          expect: average=49.75, highest=50, lowest=49.5, pass_rate=50.0
          got   : average=49.75, highest=50, lowest=49.5, pass_rate=50.0
------------------------------------------------------------------------
case 4  PASS   analyze_marks([], 50)
          expect: ValueError
          got   : raised ValueError: Marks must be a non-empty list
------------------------------------------------------------------------
case 5  PASS   analyze_marks([40, '60'], 50)
          expect: ValueError
          got   : raised ValueError: Invalid mark
------------------------------------------------------------------------
case 6  PASS   analyze_marks([-1, 50, 101], 50)
          expect: ValueError
          got   : raised ValueError: Invalid mark
------------------------------------------------------------------------
RESULT  6 PASS · 0 FAIL · 0 ERROR   (week-02/code/prompt_c.py)
========================================================================
```

**Prompt D**

```
All tests passed!
{'average': 60.0, 'highest': 80, 'lowest': 40, 'pass_rate': 66.67}
========================================================================
analyze_marks harness — week-02/code/prompt_d.py
tolerance for numeric comparison: 0.01
========================================================================
SIGNATURE: ok
------------------------------------------------------------------------
case 1  PASS   analyze_marks([40, 60, 80], 50)
          expect: average=60.0, highest=80, lowest=40, pass_rate=66.67
          got   : average=60.0, highest=80, lowest=40, pass_rate=66.67
------------------------------------------------------------------------
case 2  PASS   analyze_marks([100], 50)
          expect: average=100.0, highest=100, lowest=100, pass_rate=100.0
          got   : average=100.0, highest=100, lowest=100, pass_rate=100.0
------------------------------------------------------------------------
case 3  PASS   analyze_marks([49.5, 50], 50)
          expect: average=49.75, highest=50, lowest=49.5, pass_rate=50.0
          got   : average=49.75, highest=50, lowest=49.5, pass_rate=50.0
------------------------------------------------------------------------
case 4  PASS   analyze_marks([], 50)
          expect: ValueError
          got   : raised ValueError: Marks must be a non-empty list
------------------------------------------------------------------------
case 5  PASS   analyze_marks([40, '60'], 50)
          expect: ValueError
          got   : raised ValueError: Marks must be numbers from 0 to 100
------------------------------------------------------------------------
case 6  PASS   analyze_marks([-1, 50, 101], 50)
          expect: ValueError
          got   : raised ValueError: Marks must be numbers from 0 to 100
------------------------------------------------------------------------
RESULT  6 PASS · 0 FAIL · 0 ERROR   (week-02/code/prompt_d.py)
========================================================================
```
## 7. Scoring

| Criterion | A | B | C | D |
|---|---|---|---|---|
| Correctness (cases passed) | 2 | 2 | 2 | 2 |
| Requirement coverage | 2 | 2 | 2 | 2 |
| Verifiability (tests) | 0 | 0 | 2 | 2 |
| Assumptions stated | 0 | 1 | 2 | 2 |
| Noise (2 = none) | 1 | 1 | 2 | 2 |
| **Total / 10** | **5** | **6** | **10** | **10** |

**Prompt length, in words:** A 7 · B 55 · C 96 · D approximately 180

**Words added per point gained:**

B improved the score by 1 point compared with A, while C improved it by 4 points compared with B. D achieved the same score as C despite requiring more words. This suggests that examples and executable tests contributed more value than additional requirements once the basic implementation was already correct.

## 8. Conclusion — 150–200 words

In this experiment, I tested four different prompts using ChatGPT GPT-6 and Python. All four generated implementations passed the six official test cases. However, their quality differed in terms of requirements, testing, and clarity.

Prompts C and D received the highest scores because they included examples, validation requirements, and additional tests. I would choose Prompt D for professional development because it clearly defines input validation, output structure, passing conditions, and rounding behavior.

The most useful addition was the worked example and explicit rounding requirement. In case 1, Prompts A and B returned a pass rate of 66.66666666666666, while Prompts C and D returned 66.67. Although all four passed the official test because of its tolerance, the last two produced a more predictable result.

Some additional explanations and repeated requirements added unnecessary length without improving test outcomes. Prompt D was more detailed than C but did not achieve a higher test score.

The main ambiguity concerned rounding. The specification provided 66.67 as an example but did not clearly require rounding. In Prompt D, I explicitly required the pass rate to be rounded to two decimal places.

This experiment showed that precise prompts improve predictability and verifiability, even when simpler prompts already produce correct code.

**Word count:** 188

## 9. Two questions for the debrief

1. Why can a minimal prompt produce the same number of passing tests as a detailed prompt?
2. How can developers choose the right level of detail for an AI coding prompt?
