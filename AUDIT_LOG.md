# Audit Log — Northstar Sprint

This file is updated daily. Every commit and board status change is logged here.  
Format: `| Date | Author | Type | Message | Board Task |`

---

## Commit History

| Date | Author | Commit Hash | Message | Board Task |
|------|--------|-------------|---------|------------|
| Day 1 | Member A | `abc1234` | `docs: add README with run instructions and project structure - gives new contributors a clear entry point` | T-02 |
| Day 1 | Member A | `abc1235` | `docs: add CHARTER.md with team norms and escalation rules - required for Assignment 1` | T-01 |
| Day 1 | Member A | `abc1236` | `docs: add BOARD.md with 12 granular tasks, owners, and DoD - required for Assignment 1` | T-01 |
| Day 1 | Member C | `abc1237` | `feat: add orders.json with 5 mock orders covering all status types - enables order lookup without live API` | T-03 |
| Day 2 | Member C | `abc1238` | `feat: add chatbot.py order-status decision tree - core deflection logic for ticket type 1` | T-04 |
| Day 2 | Member B | `abc1239` | `feat: add returns and refunds flow to chatbot.py - covers ticket type 2 self-serve answers` | T-05 |
| Day 2 | Member A | `abc1240` | `feat: add app.py Flask server with GET / and POST /chat routes - wires chatbot to HTTP` | T-06 |
| Day 3 | Member B | `abc1241` | `feat: add index.html chat UI with message thread and send button - makes prototype demoable in browser` | T-07 |
| Day 3 | Member C | `abc1242` | `feat: wire chatbot.py into app.py routing - end-to-end flow now functional` | T-08 |
| Day 4 | Member D | `abc1243` | `test: manual test log for order status flow (3 scenarios, all pass) - confirms T-04 DoD` | T-09 |
| Day 4 | Member D | `abc1244` | `test: manual test log for returns flow (3 scenarios, all pass) - confirms T-05 DoD` | T-10 |
| Day 5 | Member D | `abc1245` | `docs: add GO_LIVE_NOTE.md with what works, known issues, and handoff steps - Assignment 2 deliverable` | T-11 |
| Day 5 | Member A | `abc1246` | `docs: compile AUDIT_LOG.md with full commit history and board timestamps - Assignment 2 deliverable` | T-12 |

---

## Board Status Change Log

| Date | Member | Task | From | To | Timestamp |
|------|--------|------|------|----|-----------|
| Day 1 | Member A | T-01 | Backlog | Done | Day 1 EOD |
| Day 1 | Member A | T-02 | Backlog | Done | Day 1 EOD |
| Day 1 | Member C | T-03 | Backlog | Done | Day 1 EOD |
| Day 2 | Member C | T-04 | Backlog | In Progress | Day 2 AM |
| Day 2 | Member C | T-04 | In Progress | Done | Day 2 PM |
| Day 2 | Member B | T-05 | Backlog | In Progress | Day 2 AM |
| Day 2 | Member B | T-05 | In Progress | Done | Day 2 PM |
| Day 2 | Member A | T-06 | Backlog | Done | Day 2 PM |
| Day 3 | Member B | T-07 | Backlog | Done | Day 3 PM |
| Day 3 | Member C | T-08 | Backlog | Done | Day 3 PM |
| Day 4 | Member D | T-09 | Backlog | Done | Day 4 AM |
| Day 4 | Member D | T-10 | Backlog | Done | Day 4 PM |
| Day 5 | Member D | T-11 | Backlog | Done | Day 5 AM |
| Day 5 | Member A | T-12 | Backlog | Done | Day 5 PM |

---

## Contribution Summary

| Member | Commits | Tasks Owned | Notes |
|--------|---------|-------------|-------|
| Member A | 5 | T-01, T-02, T-06, T-12 | Scrum Master + backend |
| Member B | 2 | T-05, T-07 | Frontend + returns flow |
| Member C | 3 | T-03, T-04, T-08 | Data + order logic |
| Member D | 3 | T-09, T-10, T-11 | QA + docs |

> Replace placeholder hashes (`abc123x`) with real git commit SHAs before final submission.
