# AI Usage Disclosure — Week 05

| Tool | Exact model / plan | Used for | Which files it touched |
| --- | --- | --- | --- |
| ChatGPT | GPT-6 | Planning and boundary suggestions | `lab-report.md` §2 |
| ChatGPT | GPT-6 | Initial v1 implementation | `code/original/booking_v1.py` and initial `code/booking.py` |
| ChatGPT | GPT-6 | Revising the overlap condition and preparing 24 tests | `code/booking.py`, `code/test_booking.py` |
| ChatGPT | GPT-6 | Critique and drafting report content | `lab-report.md`, this disclosure |

**The assistant wrote, or helped write, my tests in `code/`:** yes. Expected values were based on AC1–AC5; tests included day bounds, blocked room, overlapping/touching intervals, and order-preserving input checks.

**`code/original/` holds the assistant's first answer exactly as returned:** yes, as represented by the saved v1. The v1 uses inclusive overlap comparisons and differs from the final implementation. **Git-history limitation:** `code/original/booking_v1.py` was added in second commit `86fb437`, not initial commit `8d1e650`; the required commit-before-edit sequence is not demonstrated by this history.

**Everything I submitted, I can explain and defend in class — including the overlap condition:** not independently confirmed. The submission declaration currently records `no`; do not change it to `yes` without verifying your own understanding.

**Anything I accepted from the AI without fully understanding it:** review the strict comparisons, mutation check and input contract before submission.

Signed: Nurkozha
Date: 2026-10-12
