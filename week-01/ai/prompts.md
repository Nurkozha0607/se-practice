# Rocket AI — Prompt Log

## 1. Original Prompt

Build a small program that processes a list of student marks and prints:
average, highest, lowest, and pass rate.

## 2. Rocket Questions and Answers

**Initial prompt score:** 79%

**Question 1:** How will student marks be entered into the tool?

**My answer:** Paste a list of numbers (a comma-separated or line-by-line list).

**Final prompt score:** 85%

## 3. Rocket's Rewritten Prompt

A student marks analysis tool where users paste a list of numbers and instantly see computed results — average score, highest mark, lowest mark, and pass rate — displayed cleanly on a single dashboard view. The tool is lightweight, requires no login, and is designed for quick one-off use by teachers or anyone grading student work.

Building with Next.js and TypeScript.

## 4. Test Results

| Test | Input | Result | Status |
|---|---|---|---|
| A | 85, 23, 45, 90, 92 | Valid: 5, Avg: 67.00, High: 92, Low: 23, Pass: 60.0% | PASS |
| B | 88, 47, -5, 101, abc, 73, 50, , 100 | Valid: 5, Avg: 71.60, High: 100, Low: 47, Pass: 80.0% | PASS |
| C | 10, 20, 30 | Valid: 3, Avg: 20.00, High: 30, Low: 10, Pass: 0.0% | PASS |
| D | abc, , xyz | No valid marks, no crash | PASS |

*The results above represent the expected correct values. Verify that the displayed Rocket outputs match them exactly, especially decimal formatting.*

## 5. Additional Test and Defect

**Input:** 50, 49.5, 100, 0

**Expected average:** 49.88

**Actual Rocket average:** 49.9

**Issue:** The average was displayed with one decimal place instead of the required two decimal places.

Other results were correct:
- Valid marks: 4
- Highest: 100
- Lowest: 0
- Pass rate: 50.0%

## 6. Follow-up Prompt

Fix the average score formatting. The average must always display exactly two decimal places, rounded correctly. For the marks 50, 49.5, 100, 0, display 49.88 instead of 49.9. Keep all other calculations unchanged.

## 7. Fix Result

Status: FIXED

Input: 50, 49.5, 100, 0

Before fix: Average = 49.9
After fix: Average = 49.88

Rocket changed toFixed(1) to toFixed(2)
in StatsBentoGrid.tsx.

The defect was successfully fixed.
The other displayed statistics remained correct.

## 8. Extra Features Added by Rocket

- Web dashboard interface
- Next.js and TypeScript
- Configurable pass threshold slider
- Score distribution chart
- Median score
- Passing and failing student counts
- Copy results feature

## 9. Rocket Preview Link

[Add your Rocket preview or published link here.]