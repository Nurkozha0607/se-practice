# SIS #01 — Software Engineering Fundamentals, With an AI in the Loop

<!--
  This is the only file you write your report in. README.md tells you what goes where.

  Rules the checker relies on:
  - Do not delete, rename or renumber the ## headings, the ### headings, or the **Label:** words.
  - Replace every "(write here)" and "(paste here)". None may be left when you submit.
  - Comments like this one are ignored by the word counter. Delete them or leave them.
-->

**Topic:** 1.6

<!-- Exactly one of 1.1 … 1.10, e.g.  **Topic:** 1.4  -->

---

## 1. Scenario

**Question:** How should fundamental software engineering principles guide development of a small university room-booking system, and which decisions should remain with engineers rather than an AI assistant?

**Users:** Students reserving study rooms and campus administrators managing room availability.

**Problem:** Students may request the same study room at overlapping times. The service must record bookings and avoid conflicts.

**Constraints:** First, a reservation must begin in the future and last more than zero minutes but no longer than two hours. Second, a blocked room must reject new reservations, and active bookings for the same room must not overlap.

**Risk:** Two simultaneous requests might both appear valid and produce conflicting bookings if the application checks availability separately from saving the reservation.

**Assumptions:** The university, its booking website, users and traffic volumes are fictional. For this scenario, touching time intervals do not overlap, and blocking a room leaves existing bookings intact.

## 2. Analysis

Fundamental engineering principles offer a more reliable way to design this fictional Smart Campus service than starting with screens or AI-generated code. A deliberate process identifies requirements, prioritizes dependable behavior, tracks changes and reuses existing components when suitable. The objective is not to maximize the amount of code produced but to deliver a service whose decisions can be explained and tested against agreed rules.

Requirements management comes first. Students need to see free rooms, make bookings and cancel their own reservations; administrators must be able to block rooms and review usage. These goals should become distinct user stories and acceptance criteria. The two-hour limit, future-start requirement, blocked-room restriction and non-overlap rule need explicit boundary cases. For example, a booking ending at 14:00 and another starting at 14:00 should be allowed under the stated assumption. An AI assistant can propose stories and test cases, but the course scenario and the responsible engineer—not the model—determine which interpretation is approved.

The first engineering decision is to validate a booking twice at different levels. An application service checks the requested time range before attempting storage. A repository or database transaction then checks the blocked state and overlapping active bookings together with insertion. This additional implementation effort protects against the scenario's central risk: two users booking the same room concurrently. A simple availability check followed by an independent save is easier to write but may allow a race condition. The exact concurrency-control mechanism depends on the selected database; it should be tested rather than assumed correct.

The second decision is to keep the domain model small. Student, Room and Booking are sufficient core concepts, with a booking status distinguishing active from cancelled reservations. Application services can coordinate validation and confirmation without being mistaken for permanent domain relationships. Reuse is useful for standard date handling, authentication infrastructure or database transactions where those features are actually required. However, adding a large framework only because an AI suggests it could increase deployment complexity and maintenance work.

Dependability requires several forms of evidence: boundary-value tests for durations, rejection tests for blocked rooms, overlapping-booking tests and a concurrent-request test. Reviewers should also check that the system confirms only successful reservations. Passing these tests supports specified behavior under the tested conditions; it does not prove the absence of defects. Throughout development, changes to requirements must trigger updates to stories, models and tests so that the delivered behavior remains traceable.

## 3. Review

Prompt B raised twelve concrete concerns, and my proposed disposition is recorded here, subject to the student's own judgment. I accept issue 1: the process description needs scenario-specific reviews and tests. I accept issue 2, with the strongest priority: atomicity of an individual operation does not alone establish safe concurrent booking. A transaction and its isolation or database constraints require verification. I accept issue 3 because dependability also concerns availability and recovery, not merely conflict prevention. I accept issues 4 and 5: boundary-touching intervals, zero-length requests and past starts must be specified and tested. I accept issue 6: blocking a room must have an explicit policy for existing reservations.

I accept issue 7 because changes to duration limits should update requirements and tests together. I accept issue 8 but would not install a calendar library without an actual integration need. I accept issue 9: class names alone do not enforce reservation constraints. I accept issue 10 because choosing a relational database is a proposed architecture rather than a scenario fact. I accept issue 11: AI suggestions need documented comparisons with specifications, documentation and test outputs. I qualify issue 12: concurrency controls can introduce complexity, but measurable performance costs cannot be claimed without benchmarks. These trade-offs remain unmeasured.

Two substantive revisions follow from this critique. The analysis now describes concurrent safety as an implementation obligation requiring transaction-level evidence, not an automatic benefit of a named repository function. It also recommends selective reuse after considering requirements, compatibility and maintenance overhead. The SIS README, section 1, is an assignment-level source for the four-topic framing; the SIS handout, page 1, provides the required staged workflow. Neither verifies PostgreSQL transaction behavior. Until technical documentation has actually been read, the database-specific correctness claim remains unverified and qualified, not reported as proven. No deployment was tested.

## 4. Conclusion

For the fictional Smart Campus service, I recommend a requirements-led implementation with three main domain concepts, explicit booking constraints and a transactionally protected reservation operation. The development team should translate each business rule into acceptance tests, including boundary and concurrent-request cases, and keep diagrams and tests synchronized when requirements change. AI can assist with drafting models, spotting omissions and generating candidate tests, but its suggestions require review against the scenario and evidence.

The main limitation is that this report proposes an engineering approach rather than demonstrating a working database implementation. Without a chosen database and an executed concurrency test, it cannot establish that double-booking has actually been prevented. The responsible next step is a minimal prototype with reproducible tests, not an unsupported claim of complete reliability.

## 5. Reflection

Working on SIS 01 helped me understand how software engineering principles apply to a practical system. I chose the Smart Campus room booking scenario because it connects requirements, system design, and reliability in one example.

The most useful part of working with AI was comparing the initial explanation with the critical review. Prompt A gave me a structured starting point, but Prompt B identified problems that I had not considered carefully, especially concurrent bookings, incomplete acceptance criteria, and unclear assumptions.

Prompt C helped organize the suggested improvements into a more precise explanation. I learned that checking room availability before creating a booking is not necessarily sufficient when multiple requests happen simultaneously. I also understood why software requirements should describe boundary conditions, such as zero-length bookings and overlapping time intervals.

One limitation of my work is that I did not independently verify the technical claims using external documentation or execute concurrency tests. Therefore, I treated the proposed solutions as engineering recommendations rather than proven results.

In future assignments, I would define clearer requirements before using AI and verify important technical claims earlier.

## 6. References

- KBTU SITE, *SIS #01 — Software Engineering Fundamentals, With an AI in the Loop*, `sis-01/README.md`, sections 1 and 6 (supplied with the assignment; checked by the assistant, student must open these sections to claim personal verification).
- KBTU SITE, *SIS #01 Handout*, page 1, sections 1–3 (supplied PDF; checked by the assistant, student must open it before claiming personal verification).

## 7. Appendix A — Initial outline

1. Draft suggestion only (AI-assisted, not a pre-Prompt-A student outline): define booking rules as explicit acceptance criteria.
2. Draft suggestion only: use atomic storage operations to address simultaneous booking requests.
3. Draft suggestion only: keep Student, Room and Booking as a small domain model.
4. Draft suggestion only: test boundaries, blocked rooms and overlapping active bookings.
5. Draft suggestion only: reuse necessary components but independently review AI advice.

## 8. Appendix B — AI exchanges

### B1 — Draft (Prompt A)

- **Tool:** ChatGPT
- **Model:** GPT-6
- **Date:** 2026-10-12
- **Purpose:** contextual draft

**Prompt:**

~~~~text
Act as a software engineering tutor. Help me analyze topic 1.6 — Fundamental engineering principles: Apply process, dependability, requirements management and reuse to a Smart Campus room booking scenario for a first-year-level university assignment.

My scenario is a fictional university study-room booking web application used by students and administrators. Students need to reserve rooms without double bookings. Each reservation must last no longer than two hours, and blocked rooms cannot accept new bookings. The main risk is that concurrent student requests could create overlapping reservations. All university, users, and implementation details are fictional. My initial ideas are (1) define booking rules as explicit acceptance criteria; (2) use atomic storage operations for concurrent requests; (3) model Student, Room, and Booking; (4) test duration boundaries, blocked rooms, and overlaps; (5) reuse necessary components and review AI suggestions independently. These five points were prepared with AI assistance, not independently before the first commit. Draft a 400–500 word explanation using these details.

Separate facts from assumptions. Explain trade-offs and identify claims I should verify. Do not invent quotations, references or page numbers.
~~~~

**Response:**

~~~~text
# Topic 1.6 — Fundamental Engineering Principles: Smart Campus Room Booking

## 1. Introduction

Software engineering principles help developers build systems that are reliable, maintainable, and suitable for users. Four important principles are **process, dependability, requirements management, and reuse**. These principles can be applied to a fictional Smart Campus web application where students reserve university study rooms and administrators manage room availability.

## 2. Process

The process principle means following an organized approach to software development instead of writing code without planning. For Smart Campus, the development process would begin with identifying requirements, designing the system, implementing features, and testing the results.

For example, developers should define booking rules before implementation and convert them into acceptance criteria. This makes it easier to determine whether the application works correctly. A structured process requires additional planning time but can reduce mistakes and unnecessary rework.

## 3. Dependability

Dependability means ensuring that software behaves correctly and reliably, especially when problems occur. In Smart Campus, the main risk is two students booking the same room for overlapping periods.

To prevent this, the application could use database transactions and atomic operations to check availability and create reservations safely. However, simply checking availability before saving a booking may not prevent conflicts when requests arrive simultaneously. The implementation must ensure that concurrent operations cannot both create conflicting reservations.

Testing should include simultaneous booking requests, overlapping time intervals, and system failures. Stronger concurrency protection may increase implementation complexity or reduce performance, but it is important for reservation correctness.

## 4. Requirements Management

Requirements management involves identifying, documenting, validating, and maintaining system requirements.

For Smart Campus, the main requirements are:

- Students can reserve available study rooms.
- Reservations cannot exceed two hours.
- Active reservations for the same room cannot overlap.
- Blocked rooms cannot accept new reservations.

These rules should become measurable acceptance criteria. For example, a reservation lasting exactly two hours should be accepted if all other conditions are satisfied, while a reservation exceeding two hours should be rejected.

Boundary testing helps verify these requirements. Clear documentation also makes future changes easier to manage.

## 5. Reuse

Reuse means using existing software components, designs, or solutions instead of developing everything from the beginning.

Smart Campus could use reusable components for authentication, input validation, and database access. The application could also model its core entities as Student, Room, and Booking.

Reuse can save development time and improve consistency. However, reused components may introduce security vulnerabilities, compatibility problems, or unnecessary dependencies. Therefore, developers must evaluate them before integration.

AI-generated suggestions can support development, but they should be reviewed, tested, and verified independently.

## 6. Facts, Assumptions, and Verification

**Scenario facts:** The application is fictional, students reserve study rooms, reservations cannot exceed two hours, blocked rooms cannot accept new bookings, and overlapping reservations must be prevented.

**Assumptions:** The application uses a database, supports concurrent requests, and may include reusable authentication and validation components. These are proposed design choices, not confirmed implementation details.

**Claims to verify:** Whether the chosen database transaction strategy prevents overlapping bookings, whether two-hour boundary conditions work correctly, and whether reused components satisfy security and compatibility requirements.

## 7. Conclusion

Process, dependability, requirements management, and reuse work together to improve software quality. For Smart Campus, they support clear booking rules, reliable concurrent reservations, organized development, and maintainable code.

The five initial ideas in this analysis were prepared with AI assistance rather than independently before the first commit. AI was used to support planning, while its recommendations still require independent evaluation and testing.
~~~~

### B2 — Critique (Prompt B)

<!-- Prompt B is reconstructed from the instructions in our chat. Compare with the actual sent message before claiming it is verbatim. -->

- **Tool:** ChatGPT
- **Model:** GPT-6
- **Date:** 2026-10-12
- **Purpose:** critique of the earlier draft

**Prompt:**

~~~~text
Review the draft below against my chosen question and scenario. Identify inaccuracies, missing reasoning, vague claims and unsupported assumptions.
For each concern, explain why it matters and how I could check it. Include a counterexample or alternative interpretation. Do not rewrite the answer yet.
Question: Topic 1.6 — Fundamental engineering principles: How should process, dependability, requirements management and reuse be applied to a Smart Campus study-room booking system? Scenario: A fictional university web application lets students reserve study rooms and administrators block rooms. Two constraints are a maximum booking duration of two hours and no new bookings in blocked rooms. The major risk is overlapping reservations caused by concurrent requests. All university and implementation details are fictional. Draft: # Topic 1.6 — Fundamental Engineering Principles: Smart Campus Room Booking

## 1. Introduction

Software engineering principles help developers build systems that are reliable, maintainable, and suitable for users. Four important principles are **process, dependability, requirements management, and reuse**. These principles can be applied to a fictional Smart Campus web application where students reserve university study rooms and administrators manage room availability.

## 2. Process

The process principle means following an organized approach to software development instead of writing code without planning. For Smart Campus, the development process would begin with identifying requirements, designing the system, implementing features, and testing the results.

For example, developers should define booking rules before implementation and convert them into acceptance criteria. This makes it easier to determine whether the application works correctly. A structured process requires additional planning time but can reduce mistakes and unnecessary rework.

## 3. Dependability

Dependability means ensuring that software behaves correctly and reliably, especially when problems occur. In Smart Campus, the main risk is two students booking the same room for overlapping periods.

To prevent this, the application could use database transactions and atomic operations to check availability and create reservations safely. However, simply checking availability before saving a booking may not prevent conflicts when requests arrive simultaneously. The implementation must ensure that concurrent operations cannot both create conflicting reservations.

Testing should include simultaneous booking requests, overlapping time intervals, and system failures. Stronger concurrency protection may increase implementation complexity or reduce performance, but it is important for reservation correctness.

## 4. Requirements Management

Requirements management involves identifying, documenting, validating, and maintaining system requirements.

For Smart Campus, the main requirements are:

- Students can reserve available study rooms.
- Reservations cannot exceed two hours.
- Active reservations for the same room cannot overlap.
- Blocked rooms cannot accept new reservations.

These rules should become measurable acceptance criteria. For example, a reservation lasting exactly two hours should be accepted if all other conditions are satisfied, while a reservation exceeding two hours should be rejected.

Boundary testing helps verify these requirements. Clear documentation also makes future changes easier to manage.

## 5. Reuse

Reuse means using existing software components, designs, or solutions instead of developing everything from the beginning.

Smart Campus could use reusable components for authentication, input validation, and database access. The application could also model its core entities as Student, Room, and Booking.

Reuse can save development time and improve consistency. However, reused components may introduce security vulnerabilities, compatibility problems, or unnecessary dependencies. Therefore, developers must evaluate them before integration.

AI-generated suggestions can support development, but they should be reviewed, tested, and verified independently.

## 6. Facts, Assumptions, and Verification

**Scenario facts:** The application is fictional, students reserve study rooms, reservations cannot exceed two hours, blocked rooms cannot accept new bookings, and overlapping reservations must be prevented.

**Assumptions:** The application uses a database, supports concurrent requests, and may include reusable authentication and validation components. These are proposed design choices, not confirmed implementation details.

**Claims to verify:** Whether the chosen database transaction strategy prevents overlapping bookings, whether two-hour boundary conditions work correctly, and whether reused components satisfy security and compatibility requirements.

## 7. Conclusion

Process, dependability, requirements management, and reuse work together to improve software quality. For Smart Campus, they support clear booking rules, reliable concurrent reservations, organized development, and maintainable code.

The five initial ideas in this analysis were prepared with AI assistance rather than independently before the first commit. AI was used to support planning, while its recommendations still require independent evaluation and testing.
~~~~

**Response:**

~~~~text
## Review of Draft — Topic 1.6: Fundamental Engineering Principles

I reviewed the draft from the previous response against your chosen question and fictional Smart Campus scenario. The draft covers all four principles and is generally appropriate for a first-year university assignment. However, some technical statements need more precision, several design decisions are presented without sufficient justification, and the connection between the principles could be stronger.

## 1. Issues identified

| Concern                                                    | Why it matters                                                                                            | How to check it                                                                                                               | Counterexample or alternative                                                                                                     |
| ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 1. Process is described too generally.                     | The draft lists development stages but does not explain how the process helps manage booking risks.       | Define what happens during requirements review, implementation, testing, and feedback.                                        | An iterative process may identify concurrency problems earlier than a strictly sequential approach.                               |
| 2. Atomic operations are not explained precisely.          | Atomicity alone does not guarantee that two concurrent requests cannot create overlapping bookings.       | Test two simultaneous transactions requesting the same room and time. Examine transaction isolation and database constraints. | Two transactions could both observe an available room and insert conflicting bookings if concurrency is not controlled.           |
| 3. Dependability focuses mainly on correctness.            | Dependability can also include availability, security, reliability, and recovery from failures.           | Identify relevant quality attributes and define measurable checks.                                                            | A system might prevent double bookings but become unavailable during peak registration periods.                                   |
| 4. Booking overlap rules are incomplete.                   | The draft does not define whether bookings sharing an endpoint are allowed.                               | Establish an interval convention and add boundary tests.                                                                      | A booking from 10:00–11:00 and another from 11:00–12:00 could be valid if intervals are half-open.                                |
| 5. Booking duration validation is incomplete.              | Maximum duration alone does not establish whether zero-length, negative, or past bookings are valid.      | Confirm the requirements and design tests for invalid start times and durations.                                              | A booking lasting zero minutes meets the two-hour maximum but may still need rejection.                                           |
| 6. Administrator behavior is underexplained.               | Blocking a room introduces questions about existing reservations and simultaneous administrative actions. | Specify what happens when an administrator blocks a room that already has bookings.                                           | Blocking might prevent only future bookings, or it might also trigger cancellation of existing reservations.                      |
| 7. Requirements management lacks change control.           | The draft explains documentation and testing but does not show how requirements are updated and traced.   | Create a small requirements-to-tests matrix and define how changes are reviewed.                                              | Changing the maximum duration to three hours would affect validation, tests, and documentation.                                   |
| 8. Reuse examples are not sufficiently evaluated.          | Reusing components can reduce work but may introduce integration, maintenance, and security risks.        | Review component documentation, dependency versions, licenses, and relevant tests.                                            | A generic calendar library might not support room blocking or concurrency-safe reservations.                                      |
| 9. The Student, Room, and Booking model is underspecified. | Listing entities does not explain their relationships or enforce the constraints.                         | Draw a simple domain model showing booking ownership, room identity, start time, and end time.                                | A Student–Room–Booking model alone cannot prevent duplicate bookings without additional validation or storage enforcement.        |
| 10. Assumptions are partly mixed with design proposals.    | The assignment requires separating known scenario facts from unverified decisions.                        | Label each statement as a scenario fact, assumption, proposal, or verified result.                                            | A relational database is one possible solution, but another storage architecture could also enforce booking rules.                |
| 11. AI-assisted work lacks a concrete validation method.   | Saying that AI suggestions require review does not explain what independent evaluation involves.          | Compare AI claims against course materials, technical documentation, and test outcomes.                                       | AI might suggest checking availability before insertion without addressing race conditions.                                       |
| 12. Trade-offs are not compared systematically.            | The question asks how principles should be applied, not only what they mean.                              | Compare implementation effort, correctness, complexity, and maintainability for each approach.                                | Strong database locking may protect correctness but reduce concurrency, while optimistic concurrency control may require retries. |

## 2. Missing reasoning between principles

The draft discusses the four principles separately, but it should explain how they reinforce one another.

Example: preventing overlapping reservations

Requirements management

Define the no-overlap rule and its acceptance criteria

Process

Plan implementation, review risks, and schedule tests

Dependability

Enforce the rule under concurrent requests and failures

Reuse

Evaluate existing transaction and validation components

These activities influence one another rather than occurring as four isolated stages.

This connection matters because a technically correct database operation is not sufficient if the team misunderstood the booking rules or failed to test the operation under concurrency.

## 3. Claims requiring verification

The following statements should not be presented as proven outcomes without evidence.

| Draft claim                                                 | What evidence is needed?                                                                          |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Atomic storage operations prevent conflicting reservations. | Database documentation, transaction design, and concurrency test results.                         |
| A structured process reduces mistakes and rework.           | Course material or a qualified explanation that this is a potential benefit, not a guarantee.     |
| Reusable components save development time.                  | An evaluation of integration effort versus building the component.                                |
| Boundary testing verifies booking requirements.             | Specific test cases and expected results; boundary tests alone do not prove complete correctness. |
| Stronger concurrency protection reduces performance.        | Benchmarks or an explicitly qualified discussion of possible performance costs.                   |

Because the system is fictional, these can be presented as engineering expectations or risks rather than actual measured results.

## 4. Priority improvements

High

Clarify concurrency control.

Explain why a simple availability check is unsafe and how the chosen transaction or constraint approach would prevent conflicting reservations.

High

Define booking acceptance criteria.

Include duration boundaries, overlap semantics, and blocked-room behavior without presenting new assumptions as established facts.

Medium

Connect the four principles.

Show how requirements drive implementation, testing, reuse decisions, and reliability checks.

Medium

Strengthen reuse and administrator analysis.

Explain how proposed components would be evaluated and what administrator blocking means for existing reservations.

Medium

Make AI verification explicit.

Distinguish AI-generated suggestions from independently checked engineering decisions.

## 5. Overall assessment

The draft is a reasonable starting point but not yet a fully justified engineering analysis. Its strongest elements are the identification of the concurrency risk, the four required principles, and the acknowledgment of AI assistance.

The main weakness is that it often identifies a sensible technique without demonstrating why that technique would satisfy a particular requirement or what conditions could cause it to fail.

For the 400–500-word limit, prioritize the concurrency issue, precise acceptance criteria, and links between the four principles. More detailed analysis of component licensing, performance benchmarks, and alternative architectures can remain brief.

No rewrite has been made. This review identifies what to revise and how to verify the claims before submitting the assignment.
~~~~

### B3 — Revision (Prompt C)

- **Tool:** ChatGPT
- **Model:** GPT-6
- **Date:** 2026-10-12
- **Purpose:** revision using review decisions and explicitly unverified source notes

**Prompt:**

~~~~text
Revise the draft using my review decisions and source notes below. Keep the answer relevant to my scenario and preserve uncertainty where evidence is limited.

My decisions: I accept concerns 1–11 from the critical review.

1. Accept: Explain the development process through concrete requirements, design, implementation, testing, and feedback activities.
2. Accept: Clarify that atomicity alone does not prevent overlapping bookings; concurrency control and database isolation need consideration.
3. Accept: Include availability, security, reliability, and recovery as dependability concerns.
4. Accept: Define booking intervals as half-open, so touching bookings do not overlap.
5. Accept: Reject past starts, zero or negative durations, and durations longer than two hours.
6. Accept: State the fictional assumption that blocking a room prevents new bookings but keeps existing bookings.
7. Accept: Add requirements traceability and change control.
8. Accept: Explain how reusable components should be evaluated for compatibility, maintenance, and security.
9. Accept: Clarify that Student, Room, and Booking entities alone do not enforce concurrency constraints.
10. Accept: Separate scenario facts, fictional assumptions, and proposed engineering decisions.
11. Accept: Explain how AI recommendations should be checked against requirements, documentation, and tests.
12. Qualify: Compare correctness, complexity, performance, and maintainability, but do not claim measured performance costs without benchmarks.

Verified evidence: No external sources have been independently opened and verified yet. PostgreSQL documentation on transaction isolation and explicit locking has been identified as potentially relevant, but it must not be presented as verified evidence. Keep technical claims appropriately qualified. Do not invent citations, quotations, page numbers, test results, or verification outcomes.

Draft:

# Topic 1.6 — Fundamental Engineering Principles: Smart Campus Room Booking

## 1. Introduction

Software engineering principles help developers build systems that are reliable, maintainable, and suitable for users. Four important principles are **process, dependability, requirements management, and reuse**. These principles can be applied to a fictional Smart Campus web application where students reserve university study rooms and administrators manage room availability.

## 2. Process

The process principle means following an organized approach to software development instead of writing code without planning. For Smart Campus, the development process would begin with identifying requirements, designing the system, implementing features, and testing the results.

For example, developers should define booking rules before implementation and convert them into acceptance criteria. This makes it easier to determine whether the application works correctly. A structured process requires additional planning time but can reduce mistakes and unnecessary rework.

## 3. Dependability

Dependability means ensuring that software behaves correctly and reliably, especially when problems occur. In Smart Campus, the main risk is two students booking the same room for overlapping periods.

To prevent this, the application could use database transactions and atomic operations to check availability and create reservations safely. However, simply checking availability before saving a booking may not prevent conflicts when requests arrive simultaneously. The implementation must ensure that concurrent operations cannot both create conflicting reservations.

Testing should include simultaneous booking requests, overlapping time intervals, and system failures. Stronger concurrency protection may increase implementation complexity or reduce performance, but it is important for reservation correctness.

## 4. Requirements Management

Requirements management involves identifying, documenting, validating, and maintaining system requirements.

For Smart Campus, the main requirements are:

- Students can reserve available study rooms.
- Reservations cannot exceed two hours.
- Active reservations for the same room cannot overlap.
- Blocked rooms cannot accept new reservations.

These rules should become measurable acceptance criteria. For example, a reservation lasting exactly two hours should be accepted if all other conditions are satisfied, while a reservation exceeding two hours should be rejected.

Boundary testing helps verify these requirements. Clear documentation also makes future changes easier to manage.

## 5. Reuse

Reuse means using existing software components, designs, or solutions instead of developing everything from the beginning.

Smart Campus could use reusable components for authentication, input validation, and database access. The application could also model its core entities as Student, Room, and Booking.

Reuse can save development time and improve consistency. However, reused components may introduce security vulnerabilities, compatibility problems, or unnecessary dependencies. Therefore, developers must evaluate them before integration.

AI-generated suggestions can support development, but they should be reviewed, tested, and verified independently.

## 6. Facts, Assumptions, and Verification

**Scenario facts:** The application is fictional, students reserve study rooms, reservations cannot exceed two hours, blocked rooms cannot accept new bookings, and overlapping reservations must be prevented.

**Assumptions:** The application uses a database, supports concurrent requests, and may include reusable authentication and validation components. These are proposed design choices, not confirmed implementation details.

**Claims to verify:** Whether the chosen database transaction strategy prevents overlapping bookings, whether two-hour boundary conditions work correctly, and whether reused components satisfy security and compatibility requirements.

## 7. Conclusion

Process, dependability, requirements management, and reuse work together to improve software quality. For Smart Campus, they support clear booking rules, reliable concurrent reservations, organized development, and maintainable code.

The five initial ideas in this analysis were prepared with AI assistance rather than independently before the first commit. AI was used to support planning, while its recommendations still require independent evaluation and testing.

Show what you changed and why. Use only the sources I supplied. Flag remaining gaps instead of inventing details.
~~~~

**Response:**

~~~~text
Below is the revised version, followed by a summary of changes and remaining verification gaps. The explanation is approximately 445 words, excluding headings, and uses only your supplied scenario, decisions, and source notes.

## 1. Revised draft

# Topic 1.6 — Fundamental Engineering Principles: Smart Campus Room Booking

## 1. Introduction

Software engineering principles guide the development of the fictional Smart Campus study-room booking system. The four relevant principles are **process, dependability, requirements management, and reuse**.

## 2. Process

Process means organizing work into connected activities. First, developers would document booking rules and acceptance criteria. Next, they would design booking workflows and a Student–Room–Booking model, implement validation and storage logic, test ordinary and concurrent requests, and use feedback to correct defects.

An iterative approach could expose unclear rules before further development, although planning and review require effort.

## 3. Dependability

Dependability concerns correctness, availability, security, reliability, and recovery. The central risk is overlapping reservations when students submit requests simultaneously.

A basic "check then insert" operation may let both requests observe the room as free. Atomic operations alone are not a complete solution: transaction isolation, locking, or suitable database constraints would need evaluation for the chosen storage system.

The design should be tested with concurrent requests and simulated failures, including whether unsuccessful operations leave consistent booking data. Access controls should prevent students from changing others' reservations and restrict room blocking to administrators.

These measures are proposals, not implemented or verified features. Their effects on performance are unknown without benchmarks.

## 4. Requirements Management

Requirements management turns rules into testable conditions and maintains them when changes occur.

The scenario requires bookings of at most two hours, no overlapping active reservations for the same room, and no new bookings for blocked rooms.

Proposed acceptance criteria additionally reject starts in the past and durations of zero or less. Use half-open intervals [start, end), so 10:00–11:00 and 11:00–12:00 do not overlap.

A two-hour booking is permitted if other conditions hold; a longer one is rejected.

A traceability table would link each requirement to its implementation and tests, while change control would record revised rules and affected tests.

## 5. Reuse

Reuse could provide authentication, input validation, and database-access components. Developers should assess compatibility with booking rules, maintenance status, and security risks rather than assume reuse is automatically beneficial.

Student, Room, and Booking entities clarify the domain but do not themselves prevent concurrent conflicts.

The choice between custom logic and reusable components should consider correctness, complexity, maintainability, and possible performance implications without claiming measured results.

## 6. Facts, Assumptions, and Verification

**Scenario facts:** The system is fictional. The booking limits, blocking rule, and concurrency risk are given.

**Fictional assumptions:** Booking intervals are half-open, and blocking a room preserves existing reservations. Rejecting past starts and nonpositive durations are proposed requirements refinements.

**Proposed engineering decisions:** Using a database, implementing concurrency control, and selecting reusable components. These are not established implementations.

**Verification:** The five initial ideas were AI-assisted before the first commit. AI advice should be checked against requirements, official technical documentation, and reproducible tests. PostgreSQL isolation and locking documentation is a possible source to consult, not yet verified evidence.

## 7. Conclusion

Together, the four principles provide a structured approach to specifying, implementing, testing, and maintaining Smart Campus while keeping unverified design decisions explicit.

## 2. What changed and why

|   |
| - |

Section

|   |
| - |

Changes

|   |
| - |

Reason

|   |
| - |

Process

|   |
| - |

Added requirements, design, implementation, testing, and feedback

|   |
| - |

Demonstrates how the development process applies to the actual application

|   |
| - |

Dependability

|   |
| - |

Added security, availability, reliability, and recovery

|   |
| - |

Covers more than just preventing double bookings

|   |
| - |

Concurrency

|   |
| - |

Clarified the limitations of atomic operations

|   |
| - |

Avoids claiming that atomicity alone guarantees correctness

|   |
| - |

Booking rules

|   |
| - |

Introduced half-open intervals and invalid-duration checks

|   |
| - |

Makes acceptance criteria more precise

|   |
| - |

Administrator behavior

|   |
| - |

Specified that blocking preserves existing bookings

|   |
| - |

Makes the fictional assumption explicit

|   |
| - |

Requirements management

|   |
| - |

Added traceability and change control

|   |
| - |

Connects requirements with implementation and tests

|   |
| - |

Reuse

|   |
| - |

Added security, compatibility, and maintenance considerations

|   |
| - |

Explains why reusable components need evaluation

|   |
| - |

Domain model

|   |
| - |

Clarified that entities alone cannot enforce concurrency safety

|   |
| - |

Separates data modeling from technical enforcement

|   |
| - |

Evidence

|   |
| - |

Distinguished facts, assumptions, proposals, and verification

|   |
| - |

Avoids presenting untested ideas as proven outcomes

|   |
| - |

AI assistance

|   |
| - |

Retained disclosure and introduced verification steps

|   |
| - |

Demonstrates critical evaluation of AI-generated suggestions

|   |
| - |

Trade-offs

|   |
| - |

Included correctness, complexity, maintainability, and performance

|   |
| - |

Avoids unsupported claims about measured performance

## 3. Remaining gaps to verify

Concurrency implementation

The actual database, transaction isolation level, and locking or constraint mechanism remain unspecified. Verify their behavior against official documentation and concurrency tests before claiming they guarantee no overlaps.

Testing results

No actual boundary, concurrent-request, security, or failure-recovery tests have been provided. The draft correctly describes planned tests, not successful results.

Additional requirements

The behavior of existing bookings when a room is blocked, half-open intervals, past-start rejection, and positive-duration rules are your chosen assumptions or refinements, not independently verified university policies.

Documentation and references

PostgreSQL documentation was identified but not opened or checked. No external reference should be cited as verified until its relevant sections have been examined.

## 4. Final assessment

The revision addresses all 11 accepted concerns and incorporates the qualified trade-off analysis in concern 12.

It now explains how each engineering principle would be applied, rather than simply defining the principles. It also avoids inventing implementation outcomes, benchmarks, tests, and external sources.

The main limitation is the lack of independently verified technical evidence. That is clearly disclosed and does not prevent the draft from functioning as a conceptual first-year software engineering analysis.
~~~~

## 9. Appendix C — Evidence tables

### Verification table

| AI claim | Source and locator | Evidence found | Decision |
| --- | --- | --- | --- |
| Proposed check: the fundamental engineering topic covers process, dependability, requirements and reuse | SIS #01 README, section 1, topic 1.6; supplied in `sis-01/README.md` | The topic description names these four dimensions. **Assistant checked; student must independently open before claiming personal verification.** | qualify |
| Proposed check: one successful program run does not complete professional software engineering | SIS #01 README, section 6, illustrative marks-analyzer example; supplied in `sis-01/README.md` | The illustrative example identifies requirements, test evidence, instructions and maintenance as further work. **Assistant checked; student must independently open before claiming personal verification.** | qualify |

### Change log

| AI wording / suggestion | Your final version | Reason for change |
| --- | --- | --- |
| Any repository call named `tryCreateBooking` guarantees no conflicts | Concurrent safety requires a tested transactional implementation | Operation names do not establish atomicity; scenario concurrency risk |
| Reuse as many standard frameworks as possible | Reuse only infrastructure justified by actual requirements | Scenario is small; unnecessary dependencies create maintenance burden |

