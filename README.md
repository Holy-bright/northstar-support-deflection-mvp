# Northstar Support Deflection MVP

## Client

**Northstar Retail Co.**

## Project

**The Northstar Sprint — Support Deflection MVP**

## Purpose

Northstar Retail Co. is a mid-size e-commerce company whose support
team receives a high volume of repetitive customer questions.

This MVP demonstrates how automated self-service support can reduce
manual ticket handling for two high-volume support categories:

- Order status
- Returns and refunds

The MVP provides customers with immediate answers through a browser-based
chat interface without requiring a support agent for every basic question.

The project is intentionally an MVP rather than a production-ready system.
Its purpose is to prove that the support-deflection approach works and
identify what would be required for a production implementation.

---

## Team

| Team Member | GitHub Username | Role |
|---|---|---|
| Holybright Mageto | `Holy-bright` | Team Lead / Integration |
| Mary Macharia | `kayjaycloud-source` | Order Status |
| Daniel Kokonya | `dnyongesa244-pro` | Returns & Refunds |
| Charles Maina | `MainaCharles456` | Testing & Documentation |

All team members contribute through the project board, version-controlled
branches, commits, testing, documentation, and task ownership.

---

## MVP Scope

### Supported

1. **Order Status**
2. **Returns & Refunds**

### Not Currently Supported

3. **Stock Availability**

The project satisfies the MVP requirement of supporting at least two
of the three required Northstar support categories.

---

# Architecture

```text
                     ┌─────────────────────┐
                     │      Customer       │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │ Browser Chat UI     │
                     │ templates/index.html│
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │ Flask Application   │
                     │      app.py         │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │ Decision-Tree       │
                     │ Chatbot             │
                     │    chatbot.py       │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │ Mock Order Data     │
                     │ data/orders.json    │
                     └─────────────────────┘