# Project Board — Northstar Support Deflection MVP

## Northstar Sprint

**Sprint Duration:** 5 Days  
**Project:** Support Deflection MVP  
**Team Size:** 4  
**MVP Target:** Reduce manual support handling for at least 2 ticket categories:
- Order Status
- Returns & Refunds

---

## Team Members

| Member | Role / Primary Responsibility |
|---|---|
| Holybright Mageto | Project setup, Flask backend, integration, documentation |
| Mary Macharia | Chat UI, returns/refunds flow, frontend testing |
| Daniel Kokonya | Order data, chatbot logic, backend testing |
| Charles Maina | End-to-end testing, go-live readiness, audit documentation |

> Owners are responsible for completing the assigned task and updating its status on the same day work begins or finishes.

---

# Board Workflow

**BACKLOG → IN PROGRESS → DONE**

### Board Rules

- Every task must have **one clear owner**.
- No task may require more than **4 hours** of work.
- If a task grows beyond 4 hours, split it into smaller tasks.
- Each task must have a checkable **Definition of Done**.
- Task status must be updated **the same day** work starts or finishes.
- Commit messages must follow:
  
  `type: what changed - why it matters`

- Examples:
  - `feat: add order lookup flow - enables customers to check shipment status`
  - `fix: handle unknown order IDs - prevents chatbot errors`
  - `docs: update setup instructions - helps Northstar run the MVP`
- Do not use vague commit messages such as `wip`, `updates`, or `changes`.
- Every meaningful contribution must be traceable through commits, document edits, or board activity.

---

# DAY 1 — SETUP

## BACKLOG

| ID | Task | Owner | Priority | Est. | Definition of Done |
|---|---|---|---|---:|---|
| T-01 | Finalize and sign Team Charter | Holybright Mageto | High | 1h | `CHARTER.md` contains communication, deadlines, conflict-resolution, contribution, and escalation rules and is approved by all 4 members |
| T-02 | Create repository structure and project README | Holybright Mageto | High | 1h | Repository contains application folders, `README.md`, and `requirements.txt`; a new user can follow the README to run the project |
| T-03 | Create mock order dataset | Daniel Kokonya | High | 1h | `data/orders.json` contains exactly 5 valid mock orders covering processing, shipped, and delivered states |
| T-04 | Create initial project board with owners and DoD | Holybright Mageto | High | 1h | `BOARD.md` contains at least 10 granular tasks, each with owner, priority, estimate, and checkable DoD |

---

# DAY 2 — BUILD

## BACKLOG

| ID | Task | Owner | Priority | Est. | Definition of Done |
|---|---|---|---|---:|---|
| T-05 | Build order-status decision tree | Daniel Kokonya | High | 3h | `chatbot.py` accepts an order ID and returns the correct order status, tracking information when available, and delivery estimate |
| T-06 | Build returns/refunds decision tree | Mary Macharia | High | 3h | `chatbot.py` provides return eligibility, 30-day return guidance, and refund timeline responses |
| T-07 | Build Flask application routes | Holybright Mageto | High | 2h | `app.py` successfully serves `GET /` and accepts `POST /chat` requests with JSON responses |
| T-08 | Build browser chat interface | Mary Macharia | Medium | 3h | `templates/index.html` contains an input field, send control, message history, and displays chatbot responses |
| T-09 | Connect chatbot logic to Flask API | Daniel Kokonya | High | 2h | User messages submitted through `/chat` are routed to the correct order-status or returns/refunds flow |
| T-10 | Connect frontend to Flask backend | Mary Macharia | High | 2h | A user can enter a question in the browser and receive the chatbot response without manually calling the API |

---

# DAY 3 — TESTING & HARDENING

## BACKLOG

| ID | Task | Owner | Priority | Est. | Definition of Done |
|---|---|---|---|---:|---|
| T-11 | Test order-status workflow | Charles Maina | High | 1h | Three order scenarios are tested: processing, shipped, and delivered; results are recorded |
| T-12 | Test returns/refunds workflow | Charles Maina | High | 1h | Three return/refund scenarios are tested and results are recorded |
| T-13 | Test invalid and unknown order IDs | Daniel Kokonya | Medium | 1h | Invalid and unknown order IDs return a clear user-friendly response without crashing the application |
| T-14 | Test browser-to-backend end-to-end flow | Mary Macharia | High | 1h | Both supported support categories can be completed successfully from the browser |
| T-15 | Fix defects discovered during testing | Holybright Mageto | High | 3h | All critical defects discovered during testing are fixed and the affected scenarios pass again |

---

# DAY 4 — CHECKPOINT & DELIVERY PREPARATION

## BACKLOG

| ID | Task | Owner | Priority | Est. | Definition of Done |
|---|---|---|---|---:|---|
| T-16 | Review contribution and commit history | Holybright Mageto | High | 1h | Git history is reviewed and each member's meaningful contribution can be traced to project work |
| T-17 | Update board timestamps and task statuses | Charles Maina | High | 1h | Completed and active tasks have same-day status updates matching the actual work history |
| T-18 | Write go-live readiness note | Charles Maina | High | 2h | `GO_LIVE_NOTE.md` documents what works, known limitations, handoff steps, and what Northstar must do next |
| T-19 | Review README and setup instructions | Mary Macharia | Medium | 1h | README accurately describes the MVP, supported scenarios, limitations, project structure, and run instructions |
| T-20 | Perform final MVP review | All Members | High | 1h | Team confirms the prototype works end-to-end for both supported ticket categories |

---

# DAY 5 — FINAL DELIVERY

## BACKLOG

| ID | Task | Owner | Priority | Est. | Definition of Done |
|---|---|---|---|---:|---|
| T-21 | Prepare audit log | Holybright Mageto | High | 2h | `AUDIT_LOG.md` records relevant commits, authors, timestamps, task references, and board activity |
| T-22 | Final repository cleanup | Daniel Kokonya | Medium | 1h | Repository contains only required project files and no unnecessary temporary files or credentials |
| T-23 | Final end-to-end demonstration | All Members | High | 2h | Team demonstrates order-status and returns/refunds flows successfully from browser input to chatbot response |
| T-24 | Final delivery package review | All Members | High | 1h | Repository contains working MVP, README, CHARTER, BOARD, GO_LIVE_NOTE, AUDIT_LOG, source code, and mock data |
| T-25 | Final self-assessment and Peer Reliability Index | Each Member | High | 1h | Each member completes the required individual assessment and confidential Peer Reliability Index |

---

# IN PROGRESS

_Move tasks here on the same day work begins._

| ID | Task | Owner | Started | Notes |
|---|---|---|---|---|
| — | — | — | — | — |

---

# DONE

_Move tasks here immediately after completion and record the completion timestamp._

| ID | Task | Owner | Completed | Evidence / Commit |
|---|---|---|---|---|
| — | — | — | — | — |

---

# Definition of Done Standards

A task is **DONE** only when its Definition of Done has been satisfied.

A task is not considered complete simply because the code was written.

The team should be able to point to evidence such as:

- A working feature
- A passing test
- A committed document
- A Git commit
- A board status update
- A documented result

---

# Commit / Edit Audit Requirements

Every meaningful change should be traceable.

## Required Commit Format

```text
<type>: <what changed> - <why it matters>